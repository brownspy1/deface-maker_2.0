const matrix_effect = document.querySelector("#matrix-effect");
        const neo = matrix_effect.getContext("2d");
        const morpheus = (matrix_effect.width = window.innerWidth);
        const trinity = (matrix_effect.height = window.innerHeight);
    
        const str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=<>?/\\|[]`~";
        const matrix = str.split("");
    
        let font = 11;
        let col = morpheus / font;
        let arr = [];
    
        for (let i = 0; i < col; i++) arr[i] = 1;
    
        function draw() {
            neo.fillStyle = "rgba(0,0,0,.05)";
            neo.fillRect(0, 0, morpheus, trinity);
            neo.fillStyle = "#0f0";
            neo.font = font + "px system-ui";
            for (let i = 0; i < arr.length; i++) {
                let txt = matrix[Math.floor(Math.random() * matrix.length)];
                neo.fillText(txt, i * font, arr[i] * font);
                if (arr[i] * font > trinity && Math.random() > 0.975) arr[i] = 0;
                arr[i]++;
            }
        }
    
        setInterval(draw, 123);
    
        window.addEventListener("resize", () => location.reload());