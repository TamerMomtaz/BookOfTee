/* ============================================
   FLOATING KAHOTIA COMPONENT
   Add to any page with: <script src="floating-kahotia.js"></script>
   ============================================ */

(function() {
    'use strict';
    
    // ============================================
    // CONFIGURATION
    // ============================================
    const CONFIG = {
        size: 80,                    // Size of floating Kahotia
        position: 'bottom-right',    // bottom-right, bottom-left, top-right, top-left
        offset: 20,                  // Distance from edge
        glbPath: './models/two-tone_humanoid_3d_model.glb',
        enableDrag: true,
        showTooltip: true,
        linkTo: 'kahotia_cosmos.html'  // Where to go when clicked
    };
    
    // ============================================
    // INJECT STYLES
    // ============================================
    const styles = `
        /* FLOATING KAHOTIA CONTAINER */
        #floating-kahotia-container {
            position: fixed;
            width: ${CONFIG.size}px;
            height: ${CONFIG.size}px;
            z-index: 9999;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 50%;
            overflow: visible;
        }
        
        /* Position based on config */
        #floating-kahotia-container.bottom-right {
            bottom: ${CONFIG.offset}px;
            right: ${CONFIG.offset}px;
        }
        #floating-kahotia-container.bottom-left {
            bottom: ${CONFIG.offset}px;
            left: ${CONFIG.offset}px;
        }
        #floating-kahotia-container.top-right {
            top: ${CONFIG.offset}px;
            right: ${CONFIG.offset}px;
        }
        #floating-kahotia-container.top-left {
            top: ${CONFIG.offset}px;
            left: ${CONFIG.offset}px;
        }
        
        #floating-kahotia-container:hover {
            transform: scale(1.1);
        }
        
        #floating-kahotia-container.dragging {
            cursor: grabbing;
            transition: none;
        }
        
        /* CANVAS */
        #floating-kahotia-canvas {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle, #0a0a14 0%, #030308 100%);
            box-shadow: 
                0 0 20px rgba(0, 240, 255, 0.3),
                0 0 40px rgba(255, 0, 255, 0.2),
                inset 0 0 20px rgba(0, 0, 0, 0.5);
        }
        
        /* GLOW RING */
        #floating-kahotia-container::before {
            content: '';
            position: absolute;
            top: -4px;
            left: -4px;
            right: -4px;
            bottom: -4px;
            border-radius: 50%;
            background: conic-gradient(
                from 0deg,
                #00f0ff,
                #ff00ff,
                #ffd700,
                #00f0ff
            );
            animation: floatingKahotiaRingRotate 4s linear infinite;
            z-index: -1;
            opacity: 0.6;
        }
        
        @keyframes floatingKahotiaRingRotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        /* PULSE EFFECT */
        #floating-kahotia-container::after {
            content: '';
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            bottom: -10px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255, 0, 255, 0.3) 0%, transparent 70%);
            animation: floatingKahotiaPulse 2s ease-in-out infinite;
            z-index: -2;
            pointer-events: none;
        }
        
        @keyframes floatingKahotiaPulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 0.2; }
        }
        
        /* TOOLTIP */
        #floating-kahotia-tooltip {
            position: absolute;
            bottom: calc(100% + 15px);
            left: 50%;
            transform: translateX(-50%);
            background: rgba(10, 10, 20, 0.95);
            border: 1px solid rgba(0, 240, 255, 0.4);
            border-radius: 8px;
            padding: 8px 12px;
            font-family: 'Orbitron', 'Courier New', monospace;
            font-size: 0.65rem;
            color: #00f0ff;
            letter-spacing: 1px;
            white-space: nowrap;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0.3s ease;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
            pointer-events: none;
        }
        
        #floating-kahotia-tooltip::after {
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            border: 6px solid transparent;
            border-top-color: rgba(0, 240, 255, 0.4);
        }
        
        #floating-kahotia-container:hover #floating-kahotia-tooltip {
            opacity: 1;
            visibility: visible;
        }
        
        /* STATUS INDICATOR */
        #floating-kahotia-status {
            position: absolute;
            top: -5px;
            right: -5px;
            width: 16px;
            height: 16px;
            background: #00ff00;
            border-radius: 50%;
            border: 2px solid #030308;
            animation: floatingKahotiaStatusPulse 1.5s ease-in-out infinite;
        }
        
        #floating-kahotia-status.thinking {
            background: #ffd700;
        }
        
        #floating-kahotia-status.offline {
            background: #ff4444;
            animation: none;
        }
        
        @keyframes floatingKahotiaStatusPulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(0, 255, 0, 0.4); }
            50% { box-shadow: 0 0 0 6px rgba(0, 255, 0, 0); }
        }
        
        /* MOBILE ADJUSTMENTS */
        @media (max-width: 768px) {
            #floating-kahotia-container {
                width: 60px;
                height: 60px;
            }
        }
    `;
    
    // Inject styles
    const styleSheet = document.createElement('style');
    styleSheet.textContent = styles;
    document.head.appendChild(styleSheet);
    
    // ============================================
    // CREATE DOM ELEMENTS
    // ============================================
    const container = document.createElement('div');
    container.id = 'floating-kahotia-container';
    container.className = CONFIG.position;
    
    const canvas = document.createElement('canvas');
    canvas.id = 'floating-kahotia-canvas';
    container.appendChild(canvas);
    
    if (CONFIG.showTooltip) {
        const tooltip = document.createElement('div');
        tooltip.id = 'floating-kahotia-tooltip';
        tooltip.textContent = 'ENTER COSMOS';
        container.appendChild(tooltip);
    }
    
    const status = document.createElement('div');
    status.id = 'floating-kahotia-status';
    container.appendChild(status);
    
    document.body.appendChild(container);
    
    // ============================================
    // THREE.JS MINI SCENE
    // ============================================
    let scene, camera, renderer, kahotia, mixer;
    let clock = new THREE.Clock();
    
    function initThreeJS() {
        // Scene
        scene = new THREE.Scene();
        
        // Camera
        camera = new THREE.PerspectiveCamera(50, 1, 0.1, 100);
        camera.position.set(0, 0, 3);
        
        // Renderer
        renderer = new THREE.WebGLRenderer({
            canvas: canvas,
            alpha: true,
            antialias: true
        });
        renderer.setSize(CONFIG.size, CONFIG.size);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.setClearColor(0x000000, 0);
        
        // Lighting
        const ambient = new THREE.AmbientLight(0x404040, 0.5);
        scene.add(ambient);
        
        const light1 = new THREE.PointLight(0x00f0ff, 1, 10);
        light1.position.set(2, 2, 2);
        scene.add(light1);
        
        const light2 = new THREE.PointLight(0xff00ff, 0.8, 10);
        light2.position.set(-2, -1, 2);
        scene.add(light2);
        
        // Try to load GLB, fallback to procedural
        loadKahotiaModel();
    }
    
    function loadKahotiaModel() {
        if (typeof THREE.GLTFLoader === 'undefined') {
            console.log('>> GLTFLoader not available, using procedural Kahotia');
            createProceduralKahotia();
            return;
        }
        
        const loader = new THREE.GLTFLoader();
        loader.load(
            CONFIG.glbPath,
            (gltf) => {
                console.log('>> Floating Kahotia GLB loaded');
                kahotia = gltf.scene;
                kahotia.scale.set(0.8, 0.8, 0.8);
                
                // Enhance materials
                kahotia.traverse((child) => {
                    if (child.isMesh && child.material) {
                        child.material.emissive = new THREE.Color(0x1e90ff);
                        child.material.emissiveIntensity = 0.3;
                    }
                });
                
                // Setup animations
                if (gltf.animations && gltf.animations.length > 0) {
                    mixer = new THREE.AnimationMixer(kahotia);
                    gltf.animations.forEach((clip) => {
                        mixer.clipAction(clip).play();
                    });
                }
                
                scene.add(kahotia);
                animate();
            },
            undefined,
            (error) => {
                console.log('>> Floating GLB failed, using procedural:', error.message);
                createProceduralKahotia();
            }
        );
    }
    
    function createProceduralKahotia() {
        const group = new THREE.Group();
        
        // Left half - fabric (tan)
        const fabricMat = new THREE.MeshPhongMaterial({
            color: 0xd4a574,
            emissive: 0x2a1a0a,
            shininess: 10
        });
        const fabricGeo = new THREE.SphereGeometry(0.5, 32, 32, 0, Math.PI);
        const fabric = new THREE.Mesh(fabricGeo, fabricMat);
        fabric.rotation.y = -Math.PI / 2;
        group.add(fabric);
        
        // Right half - cosmic (blue)
        const cosmicMat = new THREE.MeshPhongMaterial({
            color: 0x1e90ff,
            emissive: 0x0044aa,
            emissiveIntensity: 0.5,
            shininess: 100,
            transparent: true,
            opacity: 0.9
        });
        const cosmicGeo = new THREE.SphereGeometry(0.5, 32, 32, Math.PI, Math.PI);
        const cosmic = new THREE.Mesh(cosmicGeo, cosmicMat);
        cosmic.rotation.y = -Math.PI / 2;
        group.add(cosmic);
        
        // Button eye
        const buttonGeo = new THREE.CylinderGeometry(0.08, 0.08, 0.04, 16);
        const buttonMat = new THREE.MeshPhongMaterial({ color: 0x1a1a1a });
        const button = new THREE.Mesh(buttonGeo, buttonMat);
        button.position.set(-0.25, 0.15, 0.35);
        button.rotation.x = Math.PI / 2;
        group.add(button);
        
        // Glowing eye
        const eyeGeo = new THREE.SphereGeometry(0.1, 16, 16);
        const eyeMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
        const eye = new THREE.Mesh(eyeGeo, eyeMat);
        eye.position.set(0.25, 0.15, 0.35);
        group.add(eye);
        
        kahotia = group;
        scene.add(kahotia);
        animate();
    }
    
    function animate() {
        requestAnimationFrame(animate);
        
        const delta = clock.getDelta();
        const time = clock.getElapsedTime();
        
        if (mixer) mixer.update(delta);
        
        if (kahotia) {
            kahotia.rotation.y += 0.01;
            kahotia.position.y = Math.sin(time * 2) * 0.05;
        }
        
        renderer.render(scene, camera);
    }
    
    // ============================================
    // INTERACTIONS
    // ============================================
    
    // Click to navigate
    container.addEventListener('click', (e) => {
        if (!container.classList.contains('dragging')) {
            window.location.href = CONFIG.linkTo;
        }
    });
    
    // Drag functionality
    if (CONFIG.enableDrag) {
        let isDragging = false;
        let dragStartX, dragStartY;
        let startLeft, startTop;
        let hasMoved = false;
        
        container.addEventListener('mousedown', (e) => {
            isDragging = true;
            hasMoved = false;
            dragStartX = e.clientX;
            dragStartY = e.clientY;
            
            const rect = container.getBoundingClientRect();
            startLeft = rect.left;
            startTop = rect.top;
            
            container.style.transition = 'none';
        });
        
        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            
            const dx = e.clientX - dragStartX;
            const dy = e.clientY - dragStartY;
            
            if (Math.abs(dx) > 5 || Math.abs(dy) > 5) {
                hasMoved = true;
                container.classList.add('dragging');
            }
            
            container.style.left = (startLeft + dx) + 'px';
            container.style.top = (startTop + dy) + 'px';
            container.style.right = 'auto';
            container.style.bottom = 'auto';
        });
        
        document.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                setTimeout(() => {
                    container.classList.remove('dragging');
                    container.style.transition = '';
                }, 100);
            }
        });
        
        // Touch support
        container.addEventListener('touchstart', (e) => {
            isDragging = true;
            hasMoved = false;
            dragStartX = e.touches[0].clientX;
            dragStartY = e.touches[0].clientY;
            
            const rect = container.getBoundingClientRect();
            startLeft = rect.left;
            startTop = rect.top;
            
            container.style.transition = 'none';
        });
        
        document.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            
            const dx = e.touches[0].clientX - dragStartX;
            const dy = e.touches[0].clientY - dragStartY;
            
            if (Math.abs(dx) > 5 || Math.abs(dy) > 5) {
                hasMoved = true;
                container.classList.add('dragging');
            }
            
            container.style.left = (startLeft + dx) + 'px';
            container.style.top = (startTop + dy) + 'px';
            container.style.right = 'auto';
            container.style.bottom = 'auto';
        });
        
        document.addEventListener('touchend', () => {
            if (isDragging) {
                isDragging = false;
                setTimeout(() => {
                    container.classList.remove('dragging');
                    container.style.transition = '';
                }, 100);
            }
        });
    }
    
    // ============================================
    // PUBLIC API
    // ============================================
    window.FloatingKahotia = {
        setStatus: function(state) {
            status.className = '';
            if (state === 'thinking') status.classList.add('thinking');
            if (state === 'offline') status.classList.add('offline');
        },
        setTooltip: function(text) {
            const tooltip = document.getElementById('floating-kahotia-tooltip');
            if (tooltip) tooltip.textContent = text;
        },
        hide: function() {
            container.style.display = 'none';
        },
        show: function() {
            container.style.display = 'block';
        },
        setLink: function(url) {
            CONFIG.linkTo = url;
        }
    };
    
    // ============================================
    // INITIALIZE
    // ============================================
    
    // Wait for Three.js to be available
    function waitForThreeJS() {
        if (typeof THREE !== 'undefined') {
            initThreeJS();
        } else {
            // Inject Three.js if not present
            const script = document.createElement('script');
            script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
            script.onload = () => {
                const gltfScript = document.createElement('script');
                gltfScript.src = 'https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js';
                gltfScript.onload = initThreeJS;
                document.head.appendChild(gltfScript);
            };
            document.head.appendChild(script);
        }
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', waitForThreeJS);
    } else {
        waitForThreeJS();
    }
    
})();
