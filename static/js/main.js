// CP Roaster — main.js

// ============ CUSTOM CURSOR ============
document.addEventListener('mousemove', (e) => {
  document.body.style.setProperty('--cx', e.clientX + 'px');
  document.body.style.setProperty('--cy', e.clientY + 'px');
});

// Update cursor position via pseudo-element trick
const style = document.createElement('style');
style.textContent = `body::after { left: var(--cx, -100px); top: var(--cy, -100px); }`;
document.head.appendChild(style);


// ============ LOADING MESSAGES ============
const loadingMessages = [
  "Fetching your shame...",
  "Analyzing your failures...",
  "Counting your wrong answers...",
  "Consulting the algorithm gods...",
  "Preparing your roast...",
  "This might sting a little...",
  "Almost done destroying you...",
];

let msgInterval;

function cycleLoadingMessages() {
  let i = 0;
  const el = document.getElementById('loading-text');
  if (!el) return;
  el.textContent = loadingMessages[0];
  msgInterval = setInterval(() => {
    i = (i + 1) % loadingMessages.length;
    el.textContent = loadingMessages[i];
  }, 2000);
}

function stopLoadingMessages() {
  clearInterval(msgInterval);
}


// ============ ROAST FUNCTION ============
async function startRoast() {
  const input = document.getElementById('handle-input');
  const errorEl = document.getElementById('error-msg');
  const loadingEl = document.getElementById('loading');
  const btn = document.getElementById('roast-btn');

  const handle = input.value.trim();

  // Validate
  if (!handle) {
    errorEl.textContent = '⚠ Enter a Codeforces handle first.';
    input.focus();
    return;
  }

  // Clear error
  errorEl.textContent = '';

  // Show loading
  loadingEl.classList.remove('hidden');
  btn.disabled = true;
  btn.querySelector('.btn-text').textContent = 'Roasting...';
  cycleLoadingMessages();

  try {
    const response = await fetch('/roast', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ handle })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || 'Something went wrong.');
    }

    // Store data and redirect to result page
    sessionStorage.setItem('roastData', JSON.stringify(data));
    window.location.href = '/result';

  } catch (err) {
    errorEl.textContent = '⚠ ' + err.message;
    loadingEl.classList.add('hidden');
    btn.disabled = false;
    btn.querySelector('.btn-text').textContent = 'Roast Me 🔥';
    stopLoadingMessages();
  }
}


// ============ ENTER KEY ============
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('handle-input');
  if (input) {
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') startRoast();
    });
    input.focus();
  }

  // ============ RESULT PAGE ============
  const roastContent = document.getElementById('roast-content');
  if (roastContent) {
    const raw = sessionStorage.getItem('roastData');
    if (!raw) {
      window.location.href = '/';
      return;
    }

    const data = JSON.parse(raw);

    // Fill profile
    document.getElementById('res-handle').textContent = '@' + data.handle;
    document.getElementById('res-rank').textContent = data.rank;
    document.getElementById('res-rating').textContent = data.rating;
    document.getElementById('res-max-rating').textContent = data.max_rating || data.rating;

    // Fill stats
    document.getElementById('res-solved').textContent = data.solved_count.toLocaleString();
    document.getElementById('res-acceptance').textContent = data.acceptance_rate + '%';
    document.getElementById('res-difficulty').textContent = Math.round(data.avg_difficulty);
    document.getElementById('res-contests').textContent = data.contest_count;
    document.getElementById('res-streak').textContent = data.activity_streak;
    document.getElementById('res-weak').textContent = data.weak_areas.join(', ');

    // Fill roast with typewriter effect
    typewriterEffect(roastContent, data.roast);
  }
});


// ============ TYPEWRITER EFFECT ============
function typewriterEffect(el, text) {
  el.textContent = '';
  let i = 0;
  const speed = 8; // ms per char — fast but visible

  function type() {
    if (i < text.length) {
      el.textContent += text[i];
      i++;
      setTimeout(type, speed);
    }
  }

  type();
}


// ============ COPY ROAST ============
function copyRoast() {
  const raw = sessionStorage.getItem('roastData');
  if (!raw) return;
  const data = JSON.parse(raw);

  const text = `🔥 CP Roaster — @${data.handle}\n\n${data.roast}\n\nGenerated at cp-roaster.onrender.com`;

  navigator.clipboard.writeText(text).then(() => {
    const btn = document.querySelector('.share-btn');
    btn.textContent = 'Copied! ✅';
    setTimeout(() => btn.textContent = 'Copy Roast 📋', 2000);
  });
}