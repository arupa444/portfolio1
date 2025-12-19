// Register GSAP Plugins
gsap.registerPlugin(ScrollTrigger);

// 1. Navbar Glass Effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('shadow-lg');
        navbar.classList.replace('bg-dark/80', 'bg-dark/95');
    } else {
        navbar.classList.remove('shadow-lg');
        navbar.classList.replace('bg-dark/95', 'bg-dark/80');
    }
});

// 2. Hero Animations
const tl = gsap.timeline();
tl.from('.reveal-text', {
    y: 50,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: 'power3.out'
});

// 3. Scroll Animations
const sections = document.querySelectorAll('section');

sections.forEach(section => {
    // Fade in sections
    gsap.from(section.children, {
        scrollTrigger: {
            trigger: section,
            start: 'top 80%',
            toggleActions: 'play none none reverse'
        },
        y: 50,
        opacity: 0,
        duration: 1,
        stagger: 0.1,
        ease: 'power2.out'
    });
});

// Skill Cards Stagger
gsap.from('.skill-card', {
    scrollTrigger: {
        trigger: '#skills',
        start: 'top 75%'
    },
    y: 30,
    opacity: 0,
    duration: 0.8,
    stagger: 0.1,
    ease: 'back.out(1.7)'
});

// Flash Message Dismissal
const flashContainer = document.getElementById('flash-container');
if (flashContainer) {
    const msgs = flashContainer.querySelectorAll('.flash-msg');
    msgs.forEach((msg, i) => {
        setTimeout(() => {
            msg.style.transform = 'translateX(0)';
        }, i * 200 + 100);

        setTimeout(() => {
            msg.style.transform = 'translateX(150%)';
        }, 5000); // Auto dismiss after 5s
    });
}

// 4. Canvas Neural Network Background
const canvas = document.getElementById('neural-canvas');
const ctx = canvas.getContext('2d');

let w, h, particles;
const particleCount = 60;
const connectionDistance = 150;

function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
}

class Particle {
    constructor() {
        this.x = Math.random() * w;
        this.y = Math.random() * h;
        this.vx = (Math.random() - 0.5) * 0.5;
        this.vy = (Math.random() - 0.5) * 0.5;
        this.size = Math.random() * 2;
    }
    update() {
        this.x += this.vx;
        this.y += this.vy;
        if (this.x < 0 || this.x > w) this.vx *= -1;
        if (this.y < 0 || this.y > h) this.vy *= -1;
    }
    draw() {
        ctx.fillStyle = 'rgba(59, 130, 246, 0.5)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

function initParticles() {
    particles = [];
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
}

function animateParticles() {
    ctx.clearRect(0, 0, w, h);

    particles.forEach((p, index) => {
        p.update();
        p.draw();

        // Draw connections
        for (let j = index + 1; j < particles.length; j++) {
            const p2 = particles[j];
            const dist = Math.hypot(p.x - p2.x, p.y - p2.y);

            if (dist < connectionDistance) {
                ctx.strokeStyle = `rgba(59, 130, 246, ${1 - dist / connectionDistance})`;
                ctx.lineWidth = 0.5;
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }
        }
    });
    requestAnimationFrame(animateParticles);
}

window.addEventListener('resize', resize);
resize();
initParticles();
animateParticles();

console.log("%c SYSTEM READY: Arupa Nanda Swain Portfolio ", "background: #000; color: #3b82f6; padding: 10px; font-weight: bold;");