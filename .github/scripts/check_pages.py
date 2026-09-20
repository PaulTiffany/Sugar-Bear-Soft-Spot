"""Validate the actual Jekyll output, including sharing and activity links."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from PIL import Image


class BookHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.images = []
        self.links = []
        self.canonical = None
        self.notes_closed = False
        self.in_details = False
        self.notes_image_hidden = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            self.meta[key] = attrs.get("content", "")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        elif tag == "details":
            self.in_details = True
            self.notes_closed = "open" not in attrs
        elif tag == "img":
            self.images.append(attrs)
            if attrs.get("src", "").endswith("14-big-bear-notes.png"):
                self.notes_image_hidden = self.in_details and self.notes_closed
        elif tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "details":
            self.in_details = False


def main():
    root = Path.cwd()
    site = root / "_site"
    book = BookHTML()
    book.feed((site / "index.html").read_text(encoding="utf-8"))
    page_url = "https://paultiffany.github.io/Sugar-Bear-Soft-Spot/"
    repo_url = "https://github.com/PaulTiffany/Sugar-Bear-Soft-Spot"
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    expected = sorted(p.name for p in root.glob("[0-9][0-9]-*.png"))
    actual = [Path(unquote(urlparse(im.get("src", "")).path)).name for im in book.images]
    check(actual == expected, "Built book must show every numbered page exactly once, in order.")
    check(all(im.get("alt", "").strip() for im in book.images), "Every picture needs alt text.")
    check(book.notes_image_hidden, "Big Bear Notes must start inside closed details.")
    check(book.canonical == page_url, "Canonical URL must point to the Pages book.")
    check(book.meta.get("og:url") == page_url, "Open Graph URL must point to the Pages book.")
    # Jekyll's typography may turn the title's apostrophe into a curly one.
    title = book.meta.get("og:title", "").replace("\u2019", "'")
    check(title == "Sugar Bear's Soft Spot", f"Sharing title is missing or incorrect: {title!r}.")
    check(bool(book.meta.get("og:description")), "Sharing description is missing.")
    check(book.meta.get("twitter:card") == "summary_large_image", "Twitter card must use the large image.")
    for key in ("og:image", "twitter:image"):
        check(book.meta.get(key) == page_url + "social-preview.jpg", f"Incorrect {key} URL.")
    check(bool(book.meta.get("og:image:alt")), "Sharing image needs descriptive alt text.")

    for template in ("picture-lesson.yml", "wonder.yml"):
        check(repo_url + "/issues/new?template=" + template in book.links,
              f"Activity link must open this repository's {template}.")
    for source in ("LICENSE", "NOTICE.md"):
        check(any(link.startswith(repo_url + "/blob/") and link.endswith("/.github/" + source)
                  for link in book.links), f"Automation {source} must link to GitHub.")

    for ref in book.links + [im.get("src", "") for im in book.images]:
        parsed = urlparse(urljoin(page_url, ref))
        if parsed.netloc != urlparse(page_url).netloc:
            continue
        prefix = urlparse(page_url).path
        if urlparse(ref).netloc and not parsed.path.startswith(prefix):
            continue
        if not parsed.path.startswith(prefix):
            check(False, f"Local link escapes the book's Pages path: {ref}")
            continue
        local = site / unquote(parsed.path[len(prefix):])
        check(local.exists(), f"Published link target does not exist: {ref}")

    preview = site / "social-preview.jpg"
    check(preview.is_file(), "Sharing image was not copied into the site.")
    if preview.is_file():
        check(preview.stat().st_size < 1_000_000, "Sharing image must stay under 1 MB.")
        with Image.open(preview) as image:
            image.load()
            check(image.format == "JPEG", "Sharing image must be a valid JPEG.")
            check(image.width == 2 * image.height, "Sharing image must keep its 2:1 composition.")
            check(book.meta.get("og:image:width") == str(image.width), "Sharing width metadata differs from the image.")
            check(book.meta.get("og:image:height") == str(image.height), "Sharing height metadata differs from the image.")

    for error in errors:
        print(error)
    if not errors:
        print(f"Pages checked: {len(expected)} ordered pictures, alt text, closed notes, links, and social metadata.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
