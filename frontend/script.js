/* ==========================================================================
   SCROLL RESTORATION — always start at the top on a fresh reload
   ========================================================================== */
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);
window.addEventListener('load', () => window.scrollTo(0, 0));

/* ==========================================================================
   ICONS
   ========================================================================== */
const ICONS = {
  github: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.65.5.5 5.65.5 12a11.5 11.5 0 0 0 7.86 10.93c.57.1.78-.25.78-.55v-2.1c-3.2.7-3.88-1.36-3.88-1.36-.52-1.33-1.28-1.68-1.28-1.68-1.04-.72.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.03 1.75 2.7 1.25 3.35.96.1-.75.4-1.25.73-1.53-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.29 1.18-3.09-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11 11 0 0 1 5.8 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.24 2.76.12 3.05.74.8 1.18 1.83 1.18 3.09 0 4.41-2.7 5.39-5.26 5.67.42.36.78 1.08.78 2.17v3.22c0 .3.21.66.79.55A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/></svg>`,
  kaggle: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 20.9h-3.3l-5.4-6.9-1.5 1.4v5.5H6.1V3h2.6v10l6.4-6.6h3.2l-6 6.1 6.6 8.4Z"/></svg>`,
  google: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22.1 12.2c0-.7-.06-1.4-.19-2.1H12v4h5.66c-.24 1.3-1 2.4-2.1 3.15v2.6h3.4c2-1.85 3.14-4.55 3.14-7.65Z"/><path d="M12 22c2.85 0 5.24-.94 6.98-2.55l-3.4-2.6c-.94.63-2.15 1-3.58 1-2.75 0-5.08-1.86-5.9-4.35H2.6v2.7A10 10 0 0 0 12 22Z"/><path d="M6.1 13.5a5.99 5.99 0 0 1 0-3.9V6.9H2.6a10 10 0 0 0 0 8.3l3.5-1.7Z"/><path d="M12 5.9c1.55 0 2.94.53 4.04 1.58l3.02-3C17.24 2.6 14.85 1.7 12 1.7a10 10 0 0 0-9.4 5.2l3.5 2.7c.82-2.49 3.15-4.35 5.9-3.7Z"/></svg>`,
  linkedin: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29ZM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12ZM7.12 20.45H3.56V9h3.56v11.45Z"/></svg>`,
};

/* ==========================================================================
   API HELPERS
   All content is fetched from the FastAPI backend — see backend/app/data.py
   to edit socials, experience, projects, skills, education and certificates.
   ========================================================================== */
const API_BASE = "/api";

async function fetchJSON(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`Failed to fetch ${path}: ${res.status} ${res.statusText}`);
  return res.json();
}

let CERTIFICATES = []; // populated after /api/certificates resolves

function setFormStatus(message, type = '') {
  const statusEl = document.getElementById('cf-status');
  if (!statusEl) return;
  statusEl.textContent = message;
  statusEl.className = `form-status${type ? ` ${type}` : ''}`;
}

let _scrollLockY = 0;

function lockBodyScroll() {
  _scrollLockY = window.scrollY || window.pageYOffset;
  document.body.style.position = 'fixed';
  document.body.style.top = `-${_scrollLockY}px`;
  document.body.style.left = '0';
  document.body.style.right = '0';
  document.body.style.width = '100%';
}

function unlockBodyScroll() {
  document.body.style.position = '';
  document.body.style.top = '';
  document.body.style.left = '';
  document.body.style.right = '';
  document.body.style.width = '';
  window.scrollTo(0, _scrollLockY);
}

function showContactSuccessModal() {
  const modal = document.getElementById('contactSuccessModal');
  if (!modal) return;
  lockBodyScroll();
  modal.style.display = 'flex';
  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
}

function hideContactSuccessModal() {
  const modal = document.getElementById('contactSuccessModal');
  if (!modal) return;
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  unlockBodyScroll();
}

function setFieldError(fieldId, message) {
  const field = document.getElementById(`${fieldId}-field`);
  const errorEl = document.getElementById(`${fieldId}-error`);
  if (field) field.classList.toggle('invalid', Boolean(message));
  if (errorEl) errorEl.textContent = message || '';
}

function validateContactForm() {
  const name = document.getElementById('cf-name').value.trim();
  const email = document.getElementById('cf-email').value.trim();
  const message = document.getElementById('cf-message').value.trim();

  let isValid = true;

  if (!name) {
    setFieldError('cf-name', 'This field is mandatory');
    isValid = false;
  } else {
    setFieldError('cf-name', '');
  }

  if (!email) {
    setFieldError('cf-email', 'This field is mandatory');
    isValid = false;
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    setFieldError('cf-email', 'Enter a valid email address');
    isValid = false;
  } else {
    setFieldError('cf-email', '');
  }

  if (!message) {
    setFieldError('cf-message', 'This field is mandatory');
    isValid = false;
  } else {
    setFieldError('cf-message', '');
  }

  return { isValid, name, email, message };
}

function attachContactFormHandler(emailjsConfig) {
  const form = document.getElementById('contactForm');
  const submitBtn = document.getElementById('cf-submit');
  const closeBtn = document.getElementById('contactSuccessClose');
  const successModal = document.getElementById('contactSuccessModal');
  if (!form || !submitBtn) return;

  // Clear a field's error as soon as the person starts fixing it.
  ['cf-name', 'cf-email', 'cf-message'].forEach((id) => {
    const input = document.getElementById(id);
    if (input) input.addEventListener('input', () => setFieldError(id, ''));
  });

  if (closeBtn) closeBtn.addEventListener('click', hideContactSuccessModal);
  if (successModal) successModal.addEventListener('click', (event) => {
    if (event.target === successModal) hideContactSuccessModal();
  });

  // EmailJS is initialized once, up front, rather than on every submit.
  if (window.emailjs && emailjsConfig?.public_key) {
    try { window.emailjs.init(emailjsConfig.public_key); } catch (e) { console.error('EmailJS init failed:', e); }
  }

  const handleSubmit = function (event) {
    event.preventDefault();
    event.stopImmediatePropagation();

    const { isValid, name, email, message } = validateContactForm();

    if (!isValid) {
      setFormStatus('Please fill in all mandatory fields.', 'error');
      return;
    }

    if (!window.emailjs || !emailjsConfig?.service_id || !emailjsConfig?.template_id || !emailjsConfig?.public_key) {
      setFormStatus('Contact form is not configured yet. Add your EmailJS values in the data file.', 'error');
      return;
    }

    setFormStatus('Sending...', '');

    // IMPORTANT: blur the button before disabling it. Disabling a
    // focused element makes the browser yank focus away and, combined
    // with `scroll-behavior: smooth`, causes the page to visibly jump.
    const btn = submitBtn;
    btn.blur();
    btn.disabled = true;
    btn.textContent = 'Sending...';

    // Using emailjs.send() with an explicit params object instead of
    // sendForm(). This is the fix for "it says success but the email
    // never shows up": sendForm() sends whatever the form field named
    // "email" contains as EVERY variable your template calls {{email}},
    // including the "To Email" field if your template's To Email is set
    // to {{email}} — which means the message was being routed BACK to
    // the visitor's own address instead of to Harish. to_email below is
    // hardcoded to Harish's real inbox so that can't happen, regardless
    // of what the visitor types.
    const templateParams = {
      name,
      email,
      message,
      title: message,
      from_name: name,
      from_email: email,
      reply_to: email,
      to_name: 'Harish Reddy',
      to_email: 'tanduruharishreddy@gmail.com',
    };

    window.emailjs.send(emailjsConfig.service_id, emailjsConfig.template_id, templateParams)
      .then(() => {
        btn.textContent = 'Send Message';
        setFormStatus('Message sent successfully. Harish Reddy will get back to you within 24 hours.', 'success');
        form.reset();
        ['cf-name', 'cf-email', 'cf-message'].forEach((id) => setFieldError(id, ''));
        showContactSuccessModal();
      }, (err) => {
        btn.textContent = 'Send Message';
        console.error('EmailJS send failed:', err);
        // Surface the real reason instead of a generic message, so it's
        // possible to tell what's actually misconfigured:
        //  - status 403 / "not allowed" -> add this site's domain under
        //    EmailJS dashboard > Email Services > your service > Allowed origins
        //  - status 400 / "template not found" -> template_id is wrong
        //  - status 402 -> monthly EmailJS quota used up
        //  - email "sends" (success here) but never arrives -> the
        //    template's "To Email" field in the EmailJS dashboard isn't
        //    set to your real address (it must be a fixed value there,
        //    not left blank or as a variable the form doesn't send)
        const detail = err?.text || err?.message || (typeof err === 'string' ? err : '');
        setFormStatus(
          `Unable to send the message${detail ? ` (${detail})` : ''}. Please email me directly at tanduruharishreddy@gmail.com.`,
          'error'
        );
      })
      .finally(() => {
        btn.disabled = false;
      });
  };

  form.addEventListener('submit', handleSubmit, false);
}

/* ==========================================================================
   RENDER FUNCTIONS
   ========================================================================== */
function renderSocials(containerId, socials) {
  const el = document.getElementById(containerId);
  el.innerHTML = socials.map(s => `
    <a class="social-pill" href="${s.url}" target="_blank" rel="noopener">
      ${ICONS[s.icon] || ''}<span>${s.label}</span>
    </a>`).join('');
}

function renderExperience(experience) {
  const timelineEl = document.getElementById('timeline');
  timelineEl.innerHTML = experience.map(job => `
    <div class="commit ${job.current ? 'current' : ''} reveal">
      <div class="commit-dot"></div>
      <div class="commit-head">
        <span class="commit-role">${job.role}</span>
        ${job.current ? '<span class="commit-badge">current</span>' : ''}
      </div>
      <div class="commit-meta">${job.company}<span class="dot">·</span>${job.location}<span class="dot">·</span>${job.date}</div>
      <ul class="commit-bullets">${job.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
      <div class="commit-skills">${job.skills.map(s => `<span class="chip">${s}</span>`).join('')}</div>
    </div>
  `).join('');
}

function renderProjects(projects) {
  const projectGrid = document.getElementById('projectGrid');
  projectGrid.innerHTML = projects.map(p => `
    <div class="project-card reveal">
      <h3>${p.title}</h3>
      <p>${p.blurb}</p>
      <div class="project-metrics">
        ${p.metrics.map(m => `<div><span class="metric-value">${m.value}</span><span class="metric-label">${m.label}</span></div>`).join('')}
      </div>
      <div class="project-tags">${p.tags.map(t => `<span class="chip">${t}</span>`).join('')}</div>
    </div>
  `).join('');
}

function renderSkills(skills) {
  const skillsGrid = document.getElementById('skillsGrid');
  const validGroups = (skills || [])
    .filter(g => g && Array.isArray(g.items))
    .map(g => ({ ...g, items: (g.items || []).filter(i => String(i).trim()) }))
    .filter(g => g.group && g.items.length > 0);

  skillsGrid.innerHTML = validGroups.map(g => `
    <div class="skill-group reveal">
      <h3>${g.group}</h3>
      <div class="skill-tags">${g.items.map(i => `<span class="skill-tag">${i}</span>`).join('')}</div>
    </div>
  `).join('');
}

function renderEducation(education) {
  const eduList = document.getElementById('eduList');
  eduList.innerHTML = education.map(e => `
    <div class="edu-item reveal">
      <div class="edu-main"><h3>${e.school}</h3><p>${e.degree}</p></div>
      <div class="edu-meta">${e.date}<br>${e.location}</div>
    </div>
  `).join('');
}

function renderCertificates(certificates) {
  const certGrid = document.getElementById('certGrid');
  certGrid.innerHTML = certificates.map((c, i) => `
    <a class="cert-card reveal" href="${c.link || '#'}" target="_blank" rel="noopener" data-index="${i}">
      <div class="cert-icon">📜</div>
      <h3>${c.title}</h3>
      <p>${c.issuer}</p>
      <div class="cert-cta">view link →</div>
    </a>
  `).join('');
}

function showApiError(err) {
  const message = err?.message || String(err);
  const errorHtml = `
    <div class="api-error reveal">
      <h2>Unable to load portfolio content</h2>
      <p>Please verify that the FastAPI backend is running and accessible.</p>
      <pre>${message}</pre>
    </div>
  `;

  document.getElementById('timeline').innerHTML = errorHtml;
  document.getElementById('projectGrid').innerHTML = '';
  document.getElementById('skillsGrid').innerHTML = '';
  document.getElementById('eduList').innerHTML = '';
  document.getElementById('certGrid').innerHTML = '';
}

/* ==========================================================================
   TYPED ROLE EFFECT
   ========================================================================== */
function startTypedRoles(roles) {
  const el = document.getElementById('typedRole');
  let roleIndex = 0, charIndex = 0, deleting = false;

  function tick() {
    const full = roles[roleIndex];
    if (!deleting) {
      charIndex++;
      el.textContent = full.slice(0, charIndex);
      if (charIndex === full.length) { deleting = true; setTimeout(tick, 1600); return; }
    } else {
      charIndex--;
      el.textContent = full.slice(0, charIndex);
      if (charIndex === 0) { deleting = false; roleIndex = (roleIndex + 1) % roles.length; }
    }
    setTimeout(tick, deleting ? 35 : 65);
  }
  tick();
}

/* ==========================================================================
   REVEAL ON SCROLL (re-observes elements after they're rendered from the API)
   ========================================================================== */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

function observeReveals() {
  document.querySelectorAll('.reveal:not(.in)').forEach(el => revealObserver.observe(el));
}

/* ==========================================================================
   STAT COUNTERS
   ========================================================================== */
const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const target = parseFloat(el.dataset.count);
    const isDecimal = el.dataset.count.includes('.');
    const duration = 1400;
    const start = performance.now();
    function step(now) {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      const current = target * eased;
      el.textContent = isDecimal ? current.toFixed(2) : Math.round(current);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
    statObserver.unobserve(el);
  });
}, { threshold: 0.5 });

/* ==========================================================================
   RESUME MODAL
   ========================================================================== */
const resumeModal = document.getElementById('resumeModal');
const resumeModalClose = document.getElementById('resumeModalClose');
const resumeOpenBtn = document.getElementById('resumeOpenBtn');
const resumeIframe = resumeModal ? resumeModal.querySelector('.resume-preview') : null;

function openResumeModal() {
  if (!resumeModal) return;
  // Load the PDF lazily, only when the modal is actually opened.
  if (resumeIframe && !resumeIframe.src) {
    resumeIframe.src = resumeIframe.dataset.src;
  }
  lockBodyScroll();
  resumeModal.classList.add('open');
  resumeModal.setAttribute('aria-hidden', 'false');
}

function closeResumeModal() {
  if (!resumeModal) return;
  resumeModal.classList.remove('open');
  resumeModal.setAttribute('aria-hidden', 'true');
  unlockBodyScroll();
}

if (resumeOpenBtn) resumeOpenBtn.addEventListener('click', openResumeModal);
if (resumeModalClose) resumeModalClose.addEventListener('click', closeResumeModal);
if (resumeModal) resumeModal.addEventListener('click', (e) => { if (e.target === resumeModal) closeResumeModal(); });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && resumeModal?.classList.contains('open')) closeResumeModal(); });

/* ==========================================================================
   CERTIFICATE CARD LINKS
   ========================================================================== */
document.getElementById('certGrid').addEventListener('click', (e) => {
  const card = e.target.closest('.cert-card');
  if (!card) return;
  const cert = CERTIFICATES[+card.dataset.index];
  if (cert?.link) {
    window.open(cert.link, '_blank', 'noopener,noreferrer');
  }
});

/* ==========================================================================
   NAV + SCROLL PROGRESS
   ========================================================================== */
const progressBar = document.getElementById('scrollProgress');
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const scrolled = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
  progressBar.style.width = scrolled + '%';
  navbar.classList.toggle('scrolled', h.scrollTop > 40);
}, { passive: true });

const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));

/* ==========================================================================
   AMBIENT NEURAL-NETWORK CANVAS
   ========================================================================== */
(function neuralCanvas() {
  const canvas = document.getElementById('net-canvas');
  const ctx = canvas.getContext('2d');
  let w, h, nodes;
  const NODE_COUNT_BASE = 70;

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
    const count = Math.round(NODE_COUNT_BASE * Math.min(w / 1400, 1));
    nodes = Array.from({ length: Math.max(count, 30) }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.25,
      vy: (Math.random() - 0.5) * 0.25,
      r: Math.random() * 1.6 + 0.6,
    }));
  }

  function step() {
    ctx.clearRect(0, 0, w, h);
    for (const n of nodes) {
      n.x += n.vx; n.y += n.vy;
      if (n.x < 0 || n.x > w) n.vx *= -1;
      if (n.y < 0 || n.y > h) n.vy *= -1;
    }
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j];
        const dx = a.x - b.x, dy = a.y - b.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 140) {
          ctx.strokeStyle = `rgba(62,230,196,${(1 - dist / 140) * 0.12})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }
    for (const n of nodes) {
      ctx.fillStyle = 'rgba(139,124,255,0.5)';
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
      ctx.fill();
    }
    requestAnimationFrame(step);
  }

  resize();
  window.addEventListener('resize', resize);
  step();
})();

/* ==========================================================================
   BOOTSTRAP — fetch everything from the API, then render the page
   ========================================================================== */
(async function init() {
  try {
    const [profile, certificates] = await Promise.all([
      fetchJSON('/profile'),
      fetchJSON('/certificates'),
    ]);

    CERTIFICATES = certificates;

    renderSocials('heroSocials', profile.socials);
    renderSocials('footerSocials', profile.socials);
    renderExperience(profile.experience);
    renderProjects(profile.projects);
    renderSkills(profile.skills);
    renderEducation(profile.education);
    renderCertificates(certificates);
    startTypedRoles(profile.typed_roles);
    attachContactFormHandler(profile.emailjs);

    observeReveals();
    document.querySelectorAll('.stat-num').forEach(el => statObserver.observe(el));
  } catch (err) {
    console.error('Portfolio API load error:', err);
    showApiError(err);
  }
})();