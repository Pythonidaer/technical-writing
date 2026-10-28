# Technical Writing — A Practical Field Guide

Website: https://pythonidaer.github.io/technical-writing/

Ten short technical-writing lessons with original examples, practice notes, sample answers, and browser-local review marks. The design-reading index contains 50 resources across 11 topics.

- Interactive guide: https://pythonidaer.github.io/technical-writing/
- Full text guide, including a print layout: https://pythonidaer.github.io/technical-writing/full-guide.html
- Design reading: https://pythonidaer.github.io/technical-writing/design-reading.html

The supplied technical-writing transcript is the content source. The lessons condense and clarify it; examples are illustrative. Category boundaries overlap, report conventions vary by assignment, and safety-notice colors are not universal standards. Medical examples were replaced with everyday technical examples. This is an independent learning project.

## Style guide and source alignment

The primary typography reference is the **Code Metal** entry in the independent [Website Studies](https://pythonidaer.github.io/can-i-case-study-generate-websites/) project, rather than an official Code Metal brand manual. Its measured values are snapshots, not verified brand tokens. The project adopts the font pairing and role contrast, then adapts the settings to sustained learning content.

| Area | Guide used | Application here | Why |
| --- | --- | --- | --- |
| Typography | [Code Metal study in data.js](https://github.com/Pythonidaer/can-i-case-study-generate-websites/blob/main/data.js) | DM Sans for display and reading; DM Mono for navigation, labels, and controls | Preserve the study’s proportional/monospace contrast |
| Content planning | [Toolkit content-and-tone guidance](https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/content-and-tone/best-practices.md) | Audience, task, explanation, example, practice, feedback | Give each lesson a useful outcome |
| Voice and tone | [Toolkit Mailchimp-inspired voice adaptation](https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/content-and-tone/mailchimp-tone-voice.md) | Conversational, serious, respectful, and matter-of-fact | Explain unfamiliar work without hype or condescension |
| Writing and mechanics | [Writing goals](https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/content-and-tone/mailchimp-writing-goals-principles.md) and [mechanics](https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/content-and-tone/mailchimp-grammar-mechanics.md) | Active instructions, sentence-case headings, consistent terms, US English | Make the next action predictable; adopt writing principles rather than Mailchimp’s identity |
| Composition and structure | [Toolkit AI design reset](https://github.com/Pythonidaer/llm-instruction-toolkit/tree/main/design/ai-design-reset) | Comparison panels, lesson index and reader, tables, numbered procedures | Choose structure from content relationships |
| Navigation | [Toolkit frosted-header pattern](https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/patterns/navigation/frosted-header-dropdown.md) and [Type Study decisions](https://github.com/Pythonidaer/typography-learning/blob/main/DESIGN_DECISIONS.md) | Sticky header; opaque, nonmodal dropdown at compact widths | Keep normal document scrolling and keyboard navigation |
| Action icons | [Johnny UI canonical geometry](https://github.com/Pythonidaer/design-lab/blob/main/johnny-icons.js) | Exact saved forward, menu, and close SVGs centralized in dist/icons.js | Maintain the approved action vocabulary |
| Accessibility | Semantic HTML, WCAG-oriented checks, and toolkit accessibility guidance | Landmarks, named controls, focus, reflow, text alternatives, and static reading paths | Make the content usable through more than one input or rendering mode |

### Code Metal measurements versus implemented typography

Values are CSS pixels unless stated otherwise. `size / line-height` in the reference is a computed observation; the implementation uses fluid sizes and unitless line heights. CSS weight numbers describe the selected face, not comparable visual mass across unrelated fonts.

| Role | Code Metal study | This implementation | Deliberate adjustment |
| --- | --- | --- | --- |
| Display family | DM Sans | DM Sans | Same family |
| Mono family | DM Mono | DM Mono | Same family |
| Hero | 109.04 / 88.32; weight 500; tracking −4.36px (about −0.04em) | Desktop `clamp(64px, 8.5vw, 126px)`; 137px above 1600px; line-height 0.87; weight 500; tracking −0.055em | Retain compact display emphasis while adapting to the page width |
| Mobile hero | Not established by the study | `clamp(48px, 12vw, 89px)`; line-height 0.94; tracking −0.05em | More room between wrapped lines |
| Section title | 64 / 57.6; weight 500; tracking −3.2px (−0.05em) | `clamp(38px, 4.6vw, 64px)`; line-height 0.95; weight 500; tracking −0.045em; mobile 34–46px | Keep a clear section silhouette without clipping tightly stacked text |
| Lesson title | No separate lesson role | 37–60px; line-height 1.02; weight 500; tracking −0.045em; mobile 42px | A new role for the reading interface |
| Hero supporting copy | 20 / 24; weight 300; tracking 0.6px (+0.03em) | 21px / 1.35; weight 400; tracking +0.01em; mobile 20px | Slightly heavier, looser text on the pale surface |
| Lesson body | DM Sans explanatory paragraphs | 18px / 1.6; weight 400; normal tracking; mobile 17px / 1.6 | Longer paragraphs need a more open reading rhythm |
| Navigation and actions | DM Mono 14 / 14; weight 400; tracking about +0.025–0.03em | Navigation/buttons 13px with 1.2–1.4 line-height; labels 12px / 1.5 with +0.035em | Compact metadata, with separate generous control targets |
| Reading measure | Hero supporting text in a 544px box | Hero copy up to 490px; lesson prose up to 760px; single-column full guide up to 900px including gutters | Separate introductory, instructional, and full-document reading roles |

The independent study documents Code Metal’s centered hero. This project intentionally uses a left-aligned introduction and a split instruction comparison. The typography reference does not dictate this project’s palette, navigation, content, or layout.

## Design liberties and reasons

| Area | Chosen treatment | Reason and alternative considered |
| --- | --- | --- |
| Information architecture | Foundations, explaining/instructing, then reports; persistent desktop lesson index; compact index above the mobile reader | Follow the learning dependencies. A single long page is also available as the full text guide |
| Opening composition | Large left-aligned title plus a before/after instruction comparison | Demonstrate clearer writing immediately. A centered marketing hero would explain less about the actual task |
| Layout | 1500px outer maximum, fluid gutters, narrow prose; reader/sidebar collapse below 760px | Keep orientation on desktop and a natural reading order on phones |
| Components | Native links, buttons, select/search, checkboxes, textarea, details, tables, and an SVG diagram | Familiar keyboard behavior and modest complexity; avoid a bespoke component framework |
| Icons | Johnny UI forward/menu/close; most actions remain text-only | Give navigation actions consistent geometry. The small outlined book mark is a project identity illustration, not another action-icon family |
| Color | Paper `#f2f3e9`, ink `#172d29`, dark green `#163c35`, accent `#d5ef72`, muted copy `#52605b`, rule `#c8cec1` | A calm reading surface, a strong example contrast, and a visible selected state. Color is not the only state cue |
| Spacing | Shared fluid gutters and repeated 16/24/32/48/64px relationships, with documented content-driven gaps and padding | Group related content and separate phases; avoid forcing every measurement onto a rigid grid |
| Surfaces | Rules and whitespace for most structure; bounded surfaces for comparisons, notices, and sample answers | Containers indicate actual relationships rather than enclosing every paragraph |
| Content design | Explain, show an example, offer a small task, reveal a sample, keep one rule | Make the theory usable in short sessions; do not equate a review mark with demonstrated mastery |
| Feedback | Literal saved/reviewed states; clear storage-failure wording; no congratulatory score | Confirm actual behavior without overstating learning outcomes |
| Motion | Ordinary anchor navigation and brief state changes; reduced-motion support | Keep movement subordinate to reading. No decorative reveal sequence |
| Navigation exception | Approved Johnny UI menu/close symbols in the toolkit’s nonmodal dropdown | Preserve the reference behavior while using the approved icon collection; no modal focus trap or page scroll lock |
| Persistence | Notes/review marks in localStorage; checklist resets; separate font-only service-worker cache | Useful local continuity without accounts or a server. This is not an offline copy of the entire application |
| Progressive enhancement | Prerendered resources, first lesson, and a complete standalone full text guide | Reading remains possible when JavaScript fails or is disabled |

Additional history, source scope, and verification notes are in [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md).

## Fonts, fallbacks, and caching

Reviewed [typography-learning/dist/app.js](https://github.com/Pythonidaer/typography-learning/blob/main/dist/app.js): its `ensureFont()` dynamically requests Google Fonts CSS and falls back when previews cannot load. That catalogue has many font choices; this application needs only two families. This review does **not** change the typography-learning repository or its catalogue loader.

Here, four WOFF2 faces are committed and served from the same GitHub Pages origin: DM Sans 400, 500, and 700, plus DM Mono 400. The 400/500 sans faces and mono face are preloaded directly in HTML. `fonts.css` loads through a normal stylesheet link, avoiding a nested CSS import. There are no Google Fonts runtime requests.

- Content-hashed filenames make font asset versions explicit.
- `font-display: swap` keeps text visible during first load. A brief system-font rendering is expected; hiding text to eliminate that flash would hurt reading.
- Sans fallback: `Arial, system-ui, sans-serif`. Mono fallback: `Courier New, ui-monospace, monospace`.
- On HTTPS, `font-sw.js` precaches and serves **only the four exact font URLs**. It leaves HTML, scripts, images, notes, and other requests alone. If registration/storage is unavailable, normal HTTP caching still applies.
- Update hashed filenames and bump the cache version when changing font files. Keep preload URLs, CSS, and worker paths synchronized. The worker cleans only this project’s old font-cache prefix.
- DM Sans and DM Mono are distributed under the SIL Open Font License. Both license notices are in [dist/fonts](dist/fonts).

Clearing site data also removes notes, review marks, and cached fonts. Practice notes stay in the browser and are never submitted by this application.

## Social previews and search discovery

All three HTML documents include static canonical URLs, descriptions, Open Graph metadata (including absolute image URLs, dimensions, type, and alternative text), large-image social card tags, and truthful WebPage JSON-LD. These are in the HTML source, so a social crawler does not need to execute JavaScript.

Two original 1200×630 PNG covers match the page topics. The site includes SVG/PNG favicons, an Apple touch icon, a small web manifest, robots.txt, and a sitemap with image entries. The cover is also a normal HTML image in the main guide so crawlers can discover it in page content.

This supplies preview inputs for LinkedIn/Facebook and other Open Graph consumers. Google controls indexing and whether it shows an image; metadata does not guarantee a thumbnail or ranking. Social networks may retain an older cached preview. After publication, inspect the public URL with:

- LinkedIn Post Inspector: https://www.linkedin.com/post-inspector/
- Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
- Google Rich Results Test: https://search.google.com/test/rich-results (generic WebPage markup does not itself promise a supported rich result)

Protocol reference: https://ogp.me/ . Google image guidance: https://developers.google.com/search/docs/appearance/google-images .

## Development and deployment

No package installation is required for the application. From the repository root:

```sh
node scripts/build-static.cjs
python3 scripts/check-site.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000/ . Localhost supports secure-context service workers in modern browsers; arbitrary HTTP hostnames may not. The application still renders without the font-cache enhancement.

Edit lessons in `dist/lessons.js` and resources in `dist/resources.js`. Run `node scripts/build-static.cjs` to refresh the static HTML. The build is deterministic and can run again without duplicating content.

GitHub Actions deploys `dist/` to Pages on pushes to `main`, after static rendering, JS syntax checks, and path/metadata validation. Pages source is GitHub Actions. No separate ChatGPT Sites hosting manifest or credentials are committed.

## Verification

Automated checks validate local asset paths/anchors, unique HTML IDs, metadata and canonical alignment, real WOFF2 headers, font-cache inputs, license files, cover dimensions, 10 static lessons, and 50 static resources. Browser checks and remaining limits are recorded in DESIGN_DECISIONS.md. Automated accessibility scans are useful evidence, not certification of complete WCAG conformance or native-device behavior.
