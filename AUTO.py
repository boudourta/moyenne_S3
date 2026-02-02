<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exam Grades - S3</title>
    <link rel="icon" href="https://img.icons8.com/color/48/000000/calculator.png">
    <style>
        :root {
            --primary: #008577; /* اللون الأخضر من الصورة */
            --bg: #f2f2f2;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg);
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* الهيدر العلوي */
        .app-bar {
            background-color: var(--primary);
            color: white;
            width: 100%;
            padding: 20px 0;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .container {
            width: 95%;
            max-width: 450px;
            background: white;
            margin-top: 15px;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 100px;
        }

        /* أزرار التبديل مثل الصورة */
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        .tab {
            flex: 1;
            padding: 10px;
            text-align: center;
            border-radius: 25px;
            font-weight: bold;
            font-size: 14px;
        }
        .active-tab { background: var(--primary); color: white; }
        .inactive-tab { border: 2px solid var(--primary); color: var(--primary); }

        .session-title {
            color: #555;
            font-size: 14px;
            font-weight: bold;
            margin: 15px 0 5px 5px;
        }

        /* قائمة المواد */
        .module-card {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 10px;
            border-bottom: 1px solid #eee;
        }
        .module-info { flex: 2; }
        .module-name { font-weight: 600; font-size: 15px; display: block; color: #333; }
        .module-coef { font-size: 12px; color: #888; }

        input[type="number"] {
            width: 65px;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 8px;
            text-align: center;
            font-size: 16px;
            outline: none;
        }
        input:focus { border-color: var(--primary); }

        /* زر الحساب العائم */
        .calc-btn-container {
            position: fixed;
            bottom: 20px;
            width: 95%;
            max-width: 450px;
        }
        .calc-btn {
            background-color: var(--primary);
            color: white;
            border: none;
            width: 100%;
            padding: 16px;
            border-radius: 30px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,133,119,0.3);
        }

        /* نافذة النتيجة */
        #result-modal {
            display: none;
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            background: #e0f2f1;
            border-radius: 10px;
            border-left: 5px solid var(--primary);
        }
    </style>
</head>
<body>

    <div class="app-bar">Exam Grades</div>

    <div class="container">
        <div class="tabs">
            <div class="tab active-tab">Semestre 3</div>
            <div class="tab inactive-tab">Semestre 4</div>
        </div>

        <div class="session-title">REGULAR SESSION</div>

        <div id="list-modules">
            </div>

        <div id="result-modal">
            <span style="color: #004d40; font-weight: bold;">MOYENNE GÉNÉRALE S3</span>
            <div id="moyenne-val" style="font-size: 35px; color: var(--primary); font-weight: bold;">0.00</div>
        </div>
    </div>

    <div class="calc-btn-container">
        <button class="calc-btn" onclick="calculate()">CALCULER LA MOYENNE</button>
    </div>

    <script>
        // مصفوفة المواد كما في الصورة (p1)
        const modules = [
            {n: "Energies et environnement", c: 1},
            {n: "Anglais technique", c: 1},
            {n: "Informatique 3", c: 1},
            {n: "Probabilités et statistiques", c: 2},
            {n: "TP Electronique 1 et élec...", c: 1},
            {n: "TP Ondes et Vibrations", c: 1},
            {n: "Mathématiques 3", c: 3},
            {n: "Ondes et vibrations", c: 2},
            {n: "Electronique fondament...", c: 2},
            {n: "Etat de l'art du génie éle...", c: 1},
            {n: "Electrotechnique fonda...", c: 2}
        ];

        const container = document.getElementById('list-modules');

        // بناء الواجهة برمجياً
        modules.forEach((m, i) => {
            container.innerHTML += `
                <div class="module-card">
                    <div class="module-info">
                        <span class="module-name">${m.n}</span>
                        <span class="module-coef">Coefficient: ${m.c}</span>
                    </div>
                    <input type="number" id="m-${i}" step="0.01" min="0" max="20" placeholder="00.00">
                </div>
            `;
        });

        // دالة الحساب (p3)
        function calculate() {
            let totalPts = 0;
            let totalCoeffs = 0;

            modules.forEach((m, i) => {
                let note = parseFloat(document.getElementById(`m-${i}`).value) || 0;
                totalPts += note * m.c;
                totalCoeffs += m.c;
            });

            let res = totalPts / totalCoeffs;
            document.getElementById('moyenne-val').innerText = res.toFixed(2);
            document.getElementById('result-modal').style.display = 'block';
            
            // سحب الشاشة للأسفل لرؤية النتيجة
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        }
    </script>
</body>
</html>
