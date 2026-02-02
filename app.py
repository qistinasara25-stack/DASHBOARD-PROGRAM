<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal Staff SKTB</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding: 20px;
        }

        .container {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 500px;
            padding: 30px 25px;
            text-align: center;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        #headerDepan { transition: opacity 0.3s ease; }

        .school-logo {
            width: 100px;
            height: auto;
            margin-bottom: 15px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        h2 { 
            margin-bottom: 5px; 
            color: #333; 
            font-size: 1.1rem; 
            font-weight: 700;
            line-height: 1.4;
            text-transform: uppercase;
        }
        
        p.subtitle { margin-top: 0; color: #666; font-size: 0.9rem; margin-bottom: 20px; }

        .search-box { position: relative; margin-bottom: 20px; }
        select {
            width: 100%; padding: 12px 20px; border: 2px solid #e0e0e0;
            border-radius: 15px; font-size: 1rem; outline: none; background: #fff;
            appearance: none; -webkit-appearance: none; cursor: pointer;
        }
        .dropdown-icon { position: absolute; right: 20px; top: 50%; transform: translateY(-50%); color: #764ba2; pointer-events: none; }

        #resultCard { display: none; animation: fadeIn 0.5s ease; text-align: left; }
        
        .profile-header { text-align: center; margin-bottom: 20px; }
        .profile-img {
            width: 120px; height: 120px; object-fit: cover; border-radius: 50%;
            border: 4px solid #fff; box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin: 0 auto 10px; background-color: #eee;
        }
        .teacher-name { font-size: 1.3rem; font-weight: 700; color: #333; margin: 5px 0; line-height: 1.2; }
        .teacher-role { color: #764ba2; font-weight: 600; font-size: 1rem; display: block; margin-top: 5px; }

        .tabs { display: flex; justify-content: space-between; margin-bottom: 15px; background: #f0f2f5; padding: 5px; border-radius: 12px; }
        .tab-btn {
            flex: 1; padding: 8px 5px; border: none; background: none;
            font-size: 0.75rem; 
            font-weight: 600; color: #777; cursor: pointer;
            border-radius: 8px; transition: 0.3s;
        }
        .tab-btn.active { background: #fff; color: #764ba2; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }

        .tab-content { display: none; animation: slideUp 0.3s ease; }
        .tab-content.active { display: block; }

        .info-item {
            display: flex; align-items: center; margin-bottom: 10px; padding: 12px;
            background: #f8f9fc; border-radius: 12px; border-left: 4px solid #764ba2;
        }
        .icon-box {
            min-width: 35px; height: 35px; background: #e0e7ff; color: #667eea;
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            margin-right: 12px; font-size: 1rem;
        }
        .info-content small { display: block; color: #888; font-size: 0.7rem; text-transform: uppercase; }
        .info-content span { font-weight: 500; color: #444; font-size: 0.95rem; }

        .loading-text { font-size: 0.9rem; color: #888; margin-bottom: 10px; display: none; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes slideUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

<div class="container">
    <div id="headerDepan">
        <img src="https://cdn-icons-png.flaticon.com/512/2830/2830302.png" class="school-logo" alt="Logo Sekolah">
        <h2>PORTAL GURU DAN STAFF<br>SEK. KEB. TELOK BEREMBANG</h2>
        <p class="subtitle">Sistem Maklumat Digital</p>
    </div>

    <div id="loadingMsg" class="loading-text">Sedang memuatkan data...</div>

    <div class="search-box">
        <select id="namaDropdown" onchange="pilihGuru()">
            <option value="">-- Pilih Nama Guru --</option>
        </select>
        <i class="fas fa-chevron-down dropdown-icon"></i>
    </div>

    <div id="resultCard">
        <div class="profile-header">
            <img id="pGambar" src="" class="profile-img">
            <h3 id="pNama" class="teacher-name">Nama Guru</h3>
            <span id="pJawatan" class="teacher-role">Jawatan</span>
        </div>

        <div class="tabs">
            <button class="tab-btn active" onclick="bukaTab('Info')">Info Am</button>
            <button class="tab-btn" onclick="bukaTab('Kuri')">Kurikulum</button>
            <button class="tab-btn" onclick="bukaTab('HEM')">HEM</button>
            <button class="tab-btn" onclick="bukaTab('Koko')">Koko</button>
        </div>

        <div id="Info" class="tab-content active">
            <div class="info-item">
                <div class="icon-box"><i class="fas fa-star"></i></div>
                <div class="info-content"><small>Gred Jawatan</small><span id="pGred">-</span></div>
            </div>
            <div class="info-item">
                <div class="icon-box"><i class="fas fa-id-badge"></i></div>
                <div class="info-content"><small>ID Delima</small><span id="pIdDelima">-</span></div>
            </div>
        </div>

        <div id="Kuri" class="tab-content">
            <div class="info-item">
                <div class="icon-box"><i class="fas fa-book-open"></i></div>
                <div class="info-content"><small>Opsyen Dominan</small><span id="pOpsyen">-</span></div>
            </div>
        </div>

        <div id="HEM" class="tab-content">
            <div class="info-item">
                <div class="icon-box"><i class="fas fa-user-shield"></i></div>
                <div class="info-content"><small>Tugas Khas (HEM)</small><span id="pTugasHEM">-</span></div>
            </div>
        </div>

        <div id="Koko" class="tab-content">
            <div class="info-item">
                <div class="icon-box"><i class="fas fa-running"></i></div>
                <div class="info-content"><small>Tugas Khas (Koko)</small><span id="pTugasKoko">-</span></div>
            </div>
        </div>
    </div>
</div>

<script>
    const csvUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRsvip67QwGzy2gu0coChpig9r2ZMzw6Hi6kHGnVh4m9woeC8IdZWm76AiT1kS2ugsWT3AIGNnatuBj/pub?output=csv';
    let staffData = [];

    document.getElementById('loadingMsg').style.display = 'block';

    fetch(csvUrl).then(res => res.text()).then(data => {
        const rows = data.split('\n');
        for (let i = 1; i < rows.length; i++) {
            const cols = rows[i].split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/); 
            if (cols.length > 1 && c(cols[0])) {
                staffData.push({
                    nama: c(cols[0]), jawatan: c(cols[2]), gred: c(cols[3]),
                    opsyen: c(cols[4]), idDelima: c(cols[5]), tugas: c(cols[6]), gambar: c(cols[7])
                });
            }
        }
        staffData.sort((a, b) => a.nama.localeCompare(b.nama));
        populateDropdown();
        document.getElementById('loadingMsg').style.display = 'none';
    });

    function c(text) { return text ? text.replace(/^"|"$/g, '').trim() : ''; }

    function populateDropdown() {
        const dropdown = document.getElementById('namaDropdown');
        staffData.forEach(staff => {
            const option = document.createElement('option');
            option.value = staff.nama; 
            option.textContent = staff.nama; 
            dropdown.appendChild(option);
        });
    }

    function pilihGuru() {
        const selectedName = document.getElementById('namaDropdown').value;
        const card = document.getElementById('resultCard');
        const header = document.getElementById('headerDepan');
        
        if (!selectedName) { 
            card.style.display = 'none'; 
            header.style.display = 'block'; 
            return; 
        }

        const staff = staffData.find(s => s.nama === selectedName);

        if (staff) {
            header.style.display = 'none';
            document.getElementById('pNama').textContent = staff.nama;
            document.getElementById('pJawatan').textContent = staff.jawatan;
            let imgUrl = staff.gambar && staff.gambar.length > 5 ? staff.gambar : 'https://cdn-icons-png.flaticon.com/512/847/847969.png';
            document.getElementById('pGambar').src = imgUrl;
            document.getElementById('pGred').textContent = staff.gred;
            document.getElementById('pIdDelima').textContent = staff.idDelima;
            document.getElementById('pOpsyen').textContent = staff.opsyen;
            document.getElementById('pTugasHEM').textContent = staff.tugas; 
            document.getElementById('pTugasKoko').textContent = staff.tugas; 
            card.style.display = 'block';
            bukaTab('Info');
        }
    }

    function bukaTab(tabName) {
        var i, x, tablinks;
        x = document.getElementsByClassName("tab-content");
        for (i = 0; i < x.length; i++) { x[i].style.display = "none"; }
        tablinks = document.getElementsByClassName("tab-btn");
        for (i = 0; i < tablinks.length; i++) { tablinks[i].className = tablinks[i].className.replace(" active", ""); }
        document.getElementById(tabName).style.display = "block";
        if (window.event) window.event.currentTarget.className += " active";
    }
</script>

</body>
</html>
