# Technical-writing field guide

Audience assumption: beginners and software engineers practicing technical writing. Task: understand one concept, try it, compare with a sample, and review a real draft. Source: supplied technical-writing transcript, condensed and corrected; new examples are explicitly illustrative.

Voice: conversational formality, serious humor setting, respectful, matter-of-fact enthusiasm. Warmth comes from clear examples and manageable tasks. Instructional text uses literal action verbs. Storage feedback reflects actual success and failure.

Typography: Code Metal study at Pythonidaer/can-i-case-study-generate-websites, reviewed from data.js and assets/codemetal-type.jpg. DM Sans 500 display and DM Mono 400 metadata. Study snapshot hero 109.04/88.32, tracking -4.36px; section 64/57.6, tracking -3.2px; body 20/24, weight 300; mono labels 14/14. Adaptation: responsive large headings with compact tracking; looser body line height for learning content. Font files self-hosted from Google Fonts, with system fallbacks.

Layout: green ink and pale reading surface; acid-green examples and selected states. Split before/after demonstration introduces the writing task. Lesson index and reader provide an intentional two-column structure; mobile uses a compact two-column destination list followed by a single reading column. Tables express comparisons, numbered steps express sequences. No generic feature-card grid. Frosted sticky header and opaque nonmodal mobile dropdown follow the toolkit default.

Applied toolkit: design/ai-design-reset/*, design/content-and-tone/best-practices.md, project-questions.md, mailchimp-tone-voice.md, mailchimp-writing-goals-principles.md, mailchimp-grammar-mechanics.md, patterns/navigation/frosted-header-dropdown.md. Source cloned read-only from Pythonidaer/llm-instruction-toolkit. This build does not modify either GitHub repository.

Content qualifications: physical/digital categories overlap; report conventions depend on assignment. “Examinational” is attributed to the transcript. Secondary-source reporting is valid. Survey size alone does not establish representativeness. Medical examples and device-operating advice replaced. Notice labels/colors are not presented as universal safety rules.

Interactions: hash-based lesson navigation, browser-local notes and reviewed marks, sample answer disclosure, temporary draft checklist, searchable design reading list with topic filters and shareable query parameters. No external account, server data store, or submissions. Browser-local work can be lost when site data is cleared or storage is unavailable.

Research: 50 distinct resources, mostly articles; explicitly labeled interactive explainers, standalone chapters, references, and one showcase. No video-course announcement pages. Patterns includes both visual repetition and interface/scanning patterns. Texture selections include historical examples and that age is disclosed.

## GitHub Pages, typography reliability, and accessibility (October 27, 2026)

Publication target: Pythonidaer/technical-writing, main, dist/ via GitHub Actions. The separate owner-private ChatGPT Site is not modified by this deployment. The repository was empty; initialized README, then prepared the full application and Pages workflow.

Reviewed typography-learning README, AGENTS.md, WEBSITE_DESIGN_BASELINE.md, DESIGN_DECISIONS.md, dist/app.js and its existing Pages workflow. Its dynamic Google Fonts catalogue loader is not a local font cache. For this two-family application, chose first-party WOFF2 faces, explicit preload links, direct font stylesheet loading, hash-versioned font URLs, and a narrowly scoped font-only service worker. System fallbacks and swap remain intentional during initial loading/failure. Font licenses retained. No edits were made to typography-learning.

Actions now use actual Johnny UI forward/menu/close geometry from design-lab johnny-icons.js blob 30b0dff6566203d499556bfd93b0305d60012cbb, centralized in icons.js. The book mark remains a distinct identity illustration. The menu now visibly changes to a close symbol while open.

Mobile/accessibility improvements: larger 44px lesson link targets, named keyboard-scrollable table regions, live review status, stronger focus treatment on the dark checklist, forced-colors support, wrapped long words, fluid header height for enlarged text, mobile action wrapping, safe-area clearance, and no zoom restriction. Fixed a delayed note-status update that could target a different lesson after navigation; notes persist immediately as typed.

Progressive enhancement: deterministic prerendering creates all resources and the first lesson in HTML and a complete full-guide.html. Native details elements expose sample answers in the full guide without JavaScript. An initial no-script link provides the complete reading path. The full guide includes a print layout.

Social/discovery: static canonical/Open Graph/large-image card metadata and WebPage JSON-LD on three pages; two original 1200×630 covers; accessible image descriptions; icon sizes; web manifest; robots and image sitemap. A normal HTML cover image supports image discovery. Search engines and social platforms determine indexing, preview selection, and refresh timing; those outcomes are not guaranteed by metadata.

README tables document source guides, observed Code Metal values versus implemented typography, and deliberate choices for information architecture, spacing, color, components, icons, content, motion, and persistence.

Validation before GitHub publication: static path/anchor/metadata/font/license checks passed, and all application/build JavaScript passed syntax checking. Browser QA used same-origin frames with actual CSS viewport widths of 320, 390, 768, 1080, and 1440px. The guide had no horizontal page overflow and no axe WCAG A/AA/best-practice violations at those widths. At 320px, the resource index and full guide also had no reported violations or horizontal page overflow. The full guide at 200% computed text size initially overflowed; wrapping and a content-sized header corrected that, and the repeated check had no page overflow or reported violations. Table scroll remains intentional inside named focusable regions. Manual mobile-menu checks verified open state, visible close state, Escape dismissal, and collapsed state. Previous practice/answer/progress checks were retained; immediate note persistence was source-reviewed after the targeted fix.

Axe could not resolve some contrast checks for scrolled/clipped content, so main palette text pairs were calculated independently: ink/paper 13.00:1, muted/paper 5.90:1, paper/dark 10.84:1, ink/accent 11.37:1, dark-label/dark 8.00:1. Focus/paper is 5.65:1; dark-section focus uses the light accent. These pair calculations do not constitute a full assistive-technology audit. Native iOS/Android and screen-reader testing remain outside the observed checks. Preview used an arbitrary HTTP hostname, so service-worker cache execution must be checked separately on the published HTTPS site.
