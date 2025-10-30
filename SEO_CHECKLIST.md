# 🚀 SEO Launch Checklist

A pre-launch checklist for ensuring strong technical and on-page SEO.

---

## ✅ Core SEO Setup

- [x] **Sitemap** — Dynamic XML sitemap configured (`/sitemap.xml`)
- [x] **robots.txt** — Blocks `/admin` and allows public pages
- [ ] **Canonical URLs** — `<link rel="canonical">` on all pages
- [x] **Meta Tags**
  - [x] `description`
  - [x] `keywords` (optional, low priority)
  - [x] `robots`
  - [x] `og:title`, `og:description`, `og:image`, `og:type`
  - [x] `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`
- [x] **Favicon & Manifest** — All major variants (ICO, PNG, Apple Touch, Android, manifest.json)
- [x] **Structured Data (JSON-LD)**
  - [x] `Person` or `Organization`
  - [] `Article` for blog posts
  - [ ] `BreadcrumbList`

---

## 📄 Content & On-Page

- [ ] **Unique titles & meta descriptions** for each page
- [x] **H1 tag** present and descriptive on every page
- [x] **Alt text** on all meaningful images
- [x] **Internal linking** between blog posts, case studies, and main pages
- [x] **Readable URLs** — lowercase, hyphen-separated, no query junk
- [ ] **Initial content** — at least 3 case studies + 3 blog posts live

---

## ⚙️ Technical Quality

- [ ] **HTTPS** enforced (redirect HTTP → HTTPS)
- [ ] **Custom 404 page** returns proper 404 status
- [ ] **Mobile-friendly** verified via Google test
- [ ] **Core Web Vitals**
  - [ ] Fast LCP (<2.5s)
  - [ ] Low CLS (<0.1)
  - [ ] Optimized images (WebP/AVIF)
  - [ ] Minified CSS/JS
- [ ] **Lazy-load** below-the-fold images
- [ ] **Security Headers**
  - [ ] `Strict-Transport-Security`
  - [ ] `X-Content-Type-Options: nosniff`
  - [ ] `Referrer-Policy: strict-origin-when-cross-origin`

---

## 📊 Analytics & Indexing

- [ ] **Google Analytics** tag installed (or Plausible/other)
- [ ] **Google Search Console** property verified
- [ ] **Bing Webmaster Tools** property verified
- [ ] **Submit sitemap URL** to both consoles
- [ ] **Open Graph validation**
  - [ ] [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
  - [ ] [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [ ] Test rich results with [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## 🌱 Ongoing SEO Hygiene

- [ ] Update or add content regularly (blog/case studies)
- [ ] Monitor coverage reports in Search Console
- [ ] Periodically test performance with Lighthouse
- [ ] Keep dependencies up-to-date (security & performance)
- [ ] Review internal links as content grows
- [ ] Optional: Add RSS feed for the blog

---

## After Launch

- [ ] Rewrite favicon and robots.txt from static files to root
- [ ] Update any placeholder or domain URLs to live domain
  - [ ] Meta tags
  - [ ] Sitemap URLs
  - [ ] Canonical URLs
  - [ ] robots.txt
- [ ] Update any relative URLs to absolute if needed
