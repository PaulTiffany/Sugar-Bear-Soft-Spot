# Automation provenance

The book and illustrations in this repository are licensed under CC BY 4.0.
The workflows and contribution templates under `.github/` are separately
licensed under the MIT License in this directory.

## pr-readback

The human self-review gate used by `workflows/picture-readback.yml` is the
[`Tiffany-Studios/pr-readback`](https://github.com/Tiffany-Studios/pr-readback)
GitHub Action ([Marketplace](https://github.com/marketplace/actions/pr-readback)), pinned to commit
[`1a0d7b05838c3272681dd7afdfc1821732a27140`](https://github.com/Tiffany-Studios/pr-readback/commit/1a0d7b05838c3272681dd7afdfc1821732a27140).

It supplies the bidirectional coupling between an author's self-review
attestation and the pull request's draft state. Sugar-Bear-Soft-Spot instantiates that
attestation as a responsible-grown-up readback: a child may make the lesson,
but an adult account owns the proposal and reviews what will be published. The
local picture receipt is a child-sized companion: it inventories changed
files, validates the numbered PNG pages and their reading order, checks their
README image descriptions, and reports evidence without granting authority.
The same workflow builds the Pages book and checks its rendered activity links
and social metadata. It does not deploy the site; Pages remains configured to
publish from `main`.

This book follows the flat picture-book structure, README-based Pages entry,
activities, and contribution templates in
[FuzzyCalculus](https://github.com/PaulTiffany/FuzzyCalculus) and
[Sugar-Bear-Shortcut](https://github.com/PaulTiffany/Sugar-Bear-Shortcut).

`pr-readback` is distributed under the MIT License:

> MIT License
> Copyright © 2026 Tiffany Studios
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

Upstream also records its own prior-art lineage—from the Developer Certificate
of Origin through earlier self-attestation implementations—in its
[`README`](https://github.com/Tiffany-Studios/pr-readback#prior-art).
