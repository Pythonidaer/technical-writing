# Technical Writing project instructions

Deployable source is dist/. GitHub Pages publishes it through .github/workflows/deploy-pages.yml from main. Do not import the separate ChatGPT Site's project ID, hosting manifest, or credentials.

Read README.md and DESIGN_DECISIONS.md before design changes. Typography is an intentional adaptation of the independent Code Metal study: DM Sans display/body, DM Mono navigation/labels. Preserve the current content and full text reading path.

Keep fonts first-party, versioned WOFF2 files, with OFL license notices, matching CSS declarations, preload URLs, and font-sw.js cache paths. If font files change, update the content hash and bump the font cache version. Cache only fonts; never add practice notes or API responses to that worker. Preserve system fallback stacks and font-display: swap.

Use the actual approved Johnny UI SVG geometry centralized in dist/icons.js. The book mark is an identity illustration, not an action icon. No emoji or Unicode substitute UI icons. Keep visible text labels for other actions.

Preserve keyboard focus, named controls, reduced-motion and forced-color support, semantic headings, the nonmodal mobile dropdown, and browser-local notes. Do not disable zoom. Escape returns menu focus to its trigger; hidden navigation is unfocusable. Tables must remain named keyboard-scrollable regions on narrow screens.

Run node scripts/build-static.cjs after editing lessons.js or resources.js. Do not hand-edit its generated full-guide.html or static lesson/resource blocks. Keep meaningful content available without JavaScript.

Run JavaScript syntax checks and python3 scripts/check-site.py before deployment. Check 320px, phone, tablet, desktop, enlarged text, keyboard navigation, font success/failure, and main reading states when browser QA is available. Automated checks do not establish complete WCAG conformance.

Keep canonical, Open Graph, social-card metadata, sitemap image URLs, and the 1200×630 cover images aligned with the public GitHub Pages origin. Social/search platforms control the final preview and indexing.
