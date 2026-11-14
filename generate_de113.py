import os, subprocess, pypdf

svg_cau1 = """<svg width="590" height="260" viewBox="0 0 235 105" style="background:#fff; display:block; margin:2px auto;">
  <!-- Ground -->
  <line x1="10" y1="92" x2="225" y2="92" stroke="#333" stroke-width="1.5" />
  
  <!-- Wall -->
  <line x1="180" y1="6" x2="180" y2="92" stroke="#000" stroke-width="2.5" />

  <!-- Pano (height 14 to 56) -->
  <rect x="175" y="14" width="10" height="42" fill="#bee3f8" stroke="#2b6cb0" stroke-width="1.5" />

  <!-- Observer Eye E -->
  <circle cx="35" cy="70" r="3" fill="#c53030" />
  <text x="23" y="73" font-family="Times New Roman" font-size="10" font-weight="bold" fill="#c53030">E</text>
  <line x1="35" y1="70" x2="35" y2="92" stroke="#718096" stroke-width="1" stroke-dasharray="2,2" />
  <text x="35" y="85" font-family="Times New Roman" font-size="8.5" text-anchor="middle">1,6 m</text>

  <!-- Sight lines -->
  <line x1="35" y1="70" x2="175" y2="14" stroke="#2b6cb0" stroke-width="1.2" />
  <line x1="35" y1="70" x2="175" y2="56" stroke="#2b6cb0" stroke-width="1.2" />
  <line x1="35" y1="70" x2="180" y2="70" stroke="#718096" stroke-width="1" stroke-dasharray="3,3" />

  <!-- Angle alpha -->
  <path d="M 58 66 A 25 25 0 0 0 56 70" fill="none" stroke="#e53e3e" stroke-width="1.2" />
  <text x="63" y="65" font-family="Times New Roman" font-size="10" font-style="italic" fill="#e53e3e">α</text>

  <!-- Dimension x along ground -->
  <line x1="35" y1="98" x2="180" y2="98" stroke="#4a5568" stroke-width="1" />
  <polygon points="35,98 40,96 40,100" fill="#4a5568" />
  <polygon points="180,98 175,96 175,100" fill="#4a5568" />
  <text x="107" y="97" font-family="Times New Roman" font-size="10" font-style="italic" text-anchor="middle">x</text>

  <!-- Dimensions 5,6 m and 2,6 m ON THE RIGHT (không bị đè) -->
  <!-- Top dimension 5,6 m -->
  <line x1="180" y1="14" x2="196" y2="14" stroke="#c53030" stroke-width="1" stroke-dasharray="2,2" />
  <line x1="193" y1="14" x2="193" y2="92" stroke="#c53030" stroke-width="0.8" />
  <polygon points="193,14 191,19 195,19" fill="#c53030" />
  <polygon points="193,92 191,87 195,87" fill="#c53030" />
  <text x="198" y="18" font-family="Times New Roman" font-size="9" font-weight="bold" fill="#c53030">5,6 m</text>

  <!-- Bottom dimension 2,6 m -->
  <line x1="180" y1="56" x2="196" y2="56" stroke="#c53030" stroke-width="1" stroke-dasharray="2,2" />
  <polygon points="193,56 191,61 195,61" fill="#c53030" />
  <text x="198" y="59" font-family="Times New Roman" font-size="9" font-weight="bold" fill="#c53030">2,6 m</text>
</svg>"""

svg_cau3 = """<svg width="645" height="240" viewBox="0 0 480 175" style="background:#fff; display:block; margin:2px auto;">
  <defs>
    <linearGradient id="waterGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#bee3f8" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#90cdf4" stop-opacity="0.2" />
    </linearGradient>
    <linearGradient id="archShade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fbd38d" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#feebc8" stop-opacity="0.75" />
    </linearGradient>
    <clipPath id="deckClip">
      <rect x="0" y="0" width="480" height="77" />
    </clipPath>
  </defs>

  <!-- Water area -->
  <rect x="20" y="140" width="410" height="25" fill="url(#waterGrad)" />
  <line x1="15" y1="140" x2="440" y2="140" stroke="#3182ce" stroke-width="1.5" />
  <path d="M 40 148 Q 55 145 70 148 T 100 148 T 130 148" fill="none" stroke="#63b3ed" stroke-width="1" opacity="0.7" />
  <path d="M 280 152 Q 295 149 310 152 T 340 152 T 370 152" fill="none" stroke="#63b3ed" stroke-width="1" opacity="0.7" />
  <text x="30" y="156" font-family="Times New Roman" font-size="10" font-style="italic" fill="#2b6cb0">Mặt nước</text>

  <!-- Concrete abutments / canal banks -->
  <polygon points="15,140 70,140 60,165 15,165" fill="#cbd5e0" stroke="#718096" stroke-width="1" />
  <polygon points="370,140 405,140 395,165 370,165" fill="#cbd5e0" stroke="#718096" stroke-width="1" />

  <!-- Shaded painted area: EXACT outer arch curve, clipped perfectly at deck line y=77 -->
  <path d="M 70 140 Q 220 -92 370 140 Z" fill="url(#archShade)" stroke="#dd6b20" stroke-width="1.5" clip-path="url(#deckClip)" />

  <!-- Parabolic arch (double line steel rib) -->
  <path d="M 70 140 Q 220 -92 370 140" fill="none" stroke="#2c5282" stroke-width="3.5" stroke-linecap="round" />
  <path d="M 74 140 Q 220 -80 366 140" fill="none" stroke="#2b6cb0" stroke-width="1.2" />

  <!-- Vertical suspender cables -->
  <line x1="145" y1="54" x2="145" y2="77" stroke="#4a5568" stroke-width="1" />
  <line x1="170" y1="38" x2="170" y2="77" stroke="#4a5568" stroke-width="1" />
  <line x1="195" y1="28" x2="195" y2="77" stroke="#4a5568" stroke-width="1" />
  <line x1="220" y1="25" x2="220" y2="77" stroke="#4a5568" stroke-width="1" />
  <line x1="245" y1="28" x2="245" y2="77" stroke="#4a5568" stroke-width="1" />
  <line x1="270" y1="38" x2="270" y2="77" stroke="#4a5568" stroke-width="1" />
  <line x1="295" y1="54" x2="295" y2="77" stroke="#4a5568" stroke-width="1" />

  <!-- Bridge deck (sàn cầu) - stops cleanly at abutment x=390 -->
  <rect x="25" y="77" width="365" height="6" fill="#4a5568" rx="1" />
  <line x1="25" y1="73" x2="390" y2="73" stroke="#718096" stroke-width="1.2" />
  <text x="30" y="70" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#2d3748">Sàn cầu</text>

  <!-- Labels -->
  <line x1="185" y1="48" x2="130" y2="35" stroke="#c05621" stroke-width="1" />
  <circle cx="185" cy="48" r="2" fill="#c05621" />
  <text x="125" y="33" font-family="Times New Roman" font-size="10" font-weight="bold" fill="#c05621" text-anchor="end">Phần sơn phản quang</text>

  <line x1="280" y1="22" x2="305" y2="16" stroke="#2c5282" stroke-width="1" />
  <circle cx="280" cy="22" r="2" fill="#2c5282" />
  <text x="310" y="18" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#2c5282">Vòm cầu thép</text>

  <!-- Dimension 1: Deck height 10m -->
  <line x1="400" y1="77" x2="400" y2="140" stroke="#c53030" stroke-width="1.2" />
  <polygon points="400,77 397.5,83 402.5,83" fill="#c53030" />
  <polygon points="400,140 397.5,134 402.5,134" fill="#c53030" />
  <line x1="390" y1="77" x2="408" y2="77" stroke="#c53030" stroke-width="0.8" stroke-dasharray="2,2" />
  <text x="405" y="112" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#c53030">10 m</text>

  <!-- Dimension 2: Arch total height 18m -->
  <line x1="220" y1="25" x2="220" y2="140" stroke="#2b6cb0" stroke-width="0.8" stroke-dasharray="3,3" />
  <line x1="438" y1="25" x2="438" y2="140" stroke="#2b6cb0" stroke-width="1.2" />
  <polygon points="438,25 435.5,31 440.5,31" fill="#2b6cb0" />
  <polygon points="438,140 435.5,134 440.5,134" fill="#2b6cb0" />
  <line x1="220" y1="25" x2="446" y2="25" stroke="#2b6cb0" stroke-width="0.8" stroke-dasharray="2,2" />
  <line x1="400" y1="140" x2="446" y2="140" stroke="#2b6cb0" stroke-width="0.8" stroke-dasharray="2,2" />
  <text x="444" y="85" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#2b6cb0">18 m</text>

  <!-- Dimension 3: Arch span 24m at water level -->
  <line x1="70" y1="155" x2="370" y2="155" stroke="#4a5568" stroke-width="1.2" />
  <polygon points="70,155 76,152.5 76,157.5" fill="#4a5568" />
  <polygon points="370,155 364,152.5 364,157.5" fill="#4a5568" />
  <line x1="70" y1="140" x2="70" y2="160" stroke="#718096" stroke-width="0.8" stroke-dasharray="2,2" />
  <line x1="370" y1="140" x2="370" y2="160" stroke="#718096" stroke-width="0.8" stroke-dasharray="2,2" />
  <text x="220" y="167" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#2d3748" text-anchor="middle">24 m</text>
</svg>"""

svg_cau4 = """<svg width="420" height="175" viewBox="0 0 420 175" style="background:#fff; display:block; margin:2px auto;">
  <defs>
    <linearGradient id="solidGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#90cdf4" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#ebf8ff" stop-opacity="0.1" />
    </linearGradient>
    <linearGradient id="sqGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#feebc8" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#fbd38d" stop-opacity="0.85" />
    </linearGradient>
  </defs>

  <!-- Ground shadow / base plane -->
  <ellipse cx="210" cy="142" rx="125" ry="24" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1" />

  <!-- Base circle (in perspective) -->
  <path d="M 85 142 A 125 24 0 0 1 335 142" fill="none" stroke="#2b6cb0" stroke-width="1.8" />
  <path d="M 85 142 A 125 24 0 0 0 335 142" fill="none" stroke="#a0aec0" stroke-width="1.2" stroke-dasharray="4,3" />

  <!-- Center O and diameter -->
  <line x1="85" y1="142" x2="335" y2="142" stroke="#718096" stroke-width="1" stroke-dasharray="3,3" />
  <circle cx="210" cy="142" r="2.5" fill="#2d3748" />
  <text x="212" y="155" font-family="Times New Roman" font-size="11" font-weight="bold">O</text>

  <!-- Radius dimension -->
  <line x1="210" y1="142" x2="85" y2="142" stroke="#c53030" stroke-width="1.5" />
  <circle cx="85" cy="142" r="2" fill="#c53030" />
  <text x="140" y="137" font-family="Times New Roman" font-size="10.5" font-weight="bold" fill="#c53030">R = 3 dm</text>

  <!-- 3D Outer Vault Silhouette / Dome -->
  <path d="M 85 142 Q 210 20 335 142" fill="none" stroke="#2b6cb0" stroke-width="1.8" />
  <path d="M 85 142 Q 210 20 335 142 A 125 24 0 0 1 85 142 Z" fill="url(#solidGrad)" />

  <!-- Back ridge curve -->
  <path d="M 105 130 Q 210 32 315 130" fill="none" stroke="#718096" stroke-width="1.2" stroke-dasharray="3,3" />

  <!-- A TRUE FRONT-FACING SQUARE SLICE (Thiết diện hình vuông 90 x 90) -->
  <rect x="165" y="48" width="90" height="90" fill="url(#sqGrad)" stroke="#dd6b20" stroke-width="1.8" rx="0.5" />
  
  <!-- Slab thickness / 3D depth of slice (dx = 12 px back-right) -->
  <polygon points="255,48 267,42 267,132 255,138" fill="#ed8936" fill-opacity="0.8" stroke="#dd6b20" stroke-width="1.2" />
  <polygon points="165,48 177,42 267,42 255,48" fill="#fbd38d" fill-opacity="0.9" stroke="#dd6b20" stroke-width="1.2" />

  <!-- Right-angle symbols at all 4 corners of the front square face -->
  <path d="M 165 58 L 175 58 L 175 48" fill="none" stroke="#c05621" stroke-width="1" />
  <path d="M 245 48 L 245 58 L 255 58" fill="none" stroke="#c05621" stroke-width="1" />
  <path d="M 165 128 L 175 128 L 175 138" fill="none" stroke="#c05621" stroke-width="1" />
  <path d="M 245 138 L 245 128 L 255 128" fill="none" stroke="#c05621" stroke-width="1" />

  <!-- Equal-side tick marks on width and height -->
  <line x1="208" y1="46" x2="212" y2="50" stroke="#c05621" stroke-width="1.5" />
  <line x1="208" y1="136" x2="212" y2="140" stroke="#c05621" stroke-width="1.5" />
  <line x1="163" y1="91" x2="167" y2="95" stroke="#c05621" stroke-width="1.5" />
  <line x1="253" y1="91" x2="257" y2="95" stroke="#c05621" stroke-width="1.5" />

  <!-- Labels -->
  <line x1="267" y1="80" x2="310" y2="65" stroke="#dd6b20" stroke-width="1" />
  <circle cx="267" cy="80" r="2" fill="#dd6b20" />
  <text x="315" y="62" font-family="Times New Roman" font-size="11" font-weight="bold" fill="#c05621">Thiết diện</text>
  <text x="315" y="76" font-family="Times New Roman" font-size="11" font-weight="bold" fill="#c05621">hình vuông</text>

  <line x1="120" y1="152" x2="90" y2="163" stroke="#2b6cb0" stroke-width="1" />
  <circle cx="120" cy="152" r="2" fill="#2b6cb0" />
  <text x="85" y="166" font-family="Times New Roman" font-size="10.5" font-style="italic" font-weight="bold" fill="#2b6cb0" text-anchor="end">Mặt đáy hình tròn</text>
</svg>"""

svg_kinematics = """<svg width="290" height="326" viewBox="0 0 325 365" style="background:#fff; display:block; margin:2px auto;">
  <!-- Horizontal Axis -->
  <line x1="28" y1="330" x2="273.0" y2="330" stroke="#000" stroke-width="1.2" />
  <polygon points="273.0,330 264.0,326.5 264.0,333.5" fill="#000" />
  <text x="277.0" y="335" font-family="Times New Roman" font-size="14.5" font-weight="bold" fill="#000"><tspan font-style="italic">t</tspan><tspan font-weight="normal">(s)</tspan></text>

  <!-- Vertical Axis -->
  <line x1="50" y1="348" x2="50" y2="35.0" stroke="#000" stroke-width="1.2" />
  <polygon points="50,35.0 46.5,44.0 53.5,44.0" fill="#000" />
  <text x="50" y="29.0" font-family="Times New Roman" font-size="14.5" font-weight="bold" text-anchor="middle" fill="#000"><tspan font-style="italic">v</tspan><tspan font-weight="normal">(m/s)</tspan></text>

  <!-- Origin O and perpendicular mark in 2nd quadrant -->
  <text x="35" y="345" font-family="Times New Roman" font-size="13" font-style="italic">O</text>
  <polyline points="43,330 43,323 50,323" fill="none" stroke="#000" stroke-width="0.8" />

  <!-- Horizontal dashed lines -->
  <line x1="50" y1="291.0" x2="115.0" y2="291.0" stroke="#555" stroke-width="0.85" stroke-dasharray="2.5,2.5" />
  <text x="43" y="295.0" font-family="Times New Roman" font-size="12.5" text-anchor="end">3</text>

  <text x="43" y="191.0" font-family="Times New Roman" font-size="12.5" text-anchor="end">11</text>

  <line x1="50" y1="57.0" x2="154.0" y2="57.0" stroke="#555" stroke-width="0.85" stroke-dasharray="2.5,2.5" />
  <text x="43" y="61.0" font-family="Times New Roman" font-size="12.5" text-anchor="end">21</text>

  <!-- Vertical dashed lines -->
  <line x1="89.0" y1="187.0" x2="89.0" y2="330" stroke="#555" stroke-width="0.85" stroke-dasharray="2.5,2.5" />
  <text x="89.0" y="346" font-family="Times New Roman" font-size="12.5" text-anchor="middle">3</text>

  <line x1="115.0" y1="291.0" x2="115.0" y2="330" stroke="#555" stroke-width="0.85" stroke-dasharray="2.5,2.5" />
  <text x="115.0" y="346" font-family="Times New Roman" font-size="12.5" text-anchor="middle">5</text>
  <text x="123.0" y="295.0" font-family="Times New Roman" font-size="12.5">A</text>

  <line x1="154.0" y1="57.0" x2="154.0" y2="330" stroke="#555" stroke-width="0.85" stroke-dasharray="2.5,2.5" />
  <text x="154.0" y="346" font-family="Times New Roman" font-size="12.5" text-anchor="middle">8</text>

  <text x="245.0" y="346" font-family="Times New Roman" font-size="12.5" text-anchor="middle">15</text>

  <!-- Blue Motion Curve -->
  <line x1="50" y1="187.0" x2="89.0" y2="187.0" stroke="#1d4ed8" stroke-width="2.2" />
  <path d="M 89.0,187.0 L 90.1,195.5 L 91.2,203.6 L 92.2,211.4 L 93.3,218.8 L 94.4,225.8 L 95.5,232.5 L 96.6,238.8 L 97.7,244.8 L 98.8,250.4 L 99.8,255.6 L 100.9,260.5 L 102.0,265.0 L 103.1,269.2 L 104.2,272.9 L 105.2,276.4 L 106.3,279.4 L 107.4,282.2 L 108.5,284.5 L 109.6,286.5 L 110.7,288.1 L 111.8,289.4 L 112.8,290.3 L 113.9,290.8 L 115.0,291.0 L 116.1,290.8 L 117.2,290.3 L 118.2,289.4 L 119.3,288.1 L 120.4,286.5 L 121.5,284.5 L 122.6,282.2 L 123.7,279.4 L 124.8,276.4 L 125.8,272.9 L 126.9,269.2 L 128.0,265.0 L 129.1,260.5 L 130.2,255.6 L 131.2,250.4 L 132.3,244.8 L 133.4,238.8 L 134.5,232.5 L 135.6,225.8 L 136.7,218.8 L 137.8,211.4 L 138.8,203.6 L 139.9,195.5 L 141.0,187.0 L 142.1,178.2 L 143.2,168.9 L 144.2,159.4 L 145.3,149.4 L 146.4,139.2 L 147.5,128.5 L 148.6,117.5 L 149.7,106.1 L 150.8,94.4 L 151.8,82.3 L 152.9,69.8 L 154.0,57.0" fill="none" stroke="#1d4ed8" stroke-width="2.2" />
  <line x1="154.0" y1="57.0" x2="245.0" y2="330" stroke="#1d4ed8" stroke-width="2.2" />
</svg>"""

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Kỳ khảo sát chất lượng lớp 12 - Môn Toán (Mã đề: 113)</title>
<!-- KaTeX -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
@page {{
  size: A4;
  margin-top: 5mm;
  margin-bottom: 5mm;
  margin-left: 11.5mm;
  margin-right: 11.5mm;
  @bottom-right {{
    content: "Trang " counter(page) "/" counter(pages) " – Mã đề: 113";
    font-family: 'Times New Roman', serif;
    font-size: 9pt;
    color: #000;
  }}
}}

body {{
  font-family: 'Times New Roman', serif;
  font-size: 10pt;
  line-height: 1.25;
  color: #000;
  margin: 0;
  padding: 0;
}}

.katex .accent-vec > svg {{
  transform: scale(1.4);
  transform-origin: center bottom;
}}
.katex .svg-align > svg {{
  transform: scale(1.25);
  transform-origin: center bottom;
}}

.header-table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 2px;
}}
.header-table td {{
  vertical-align: top;
  padding: 0;
}}
.left-header {{
  width: 44%;
  text-align: center;
}}
.right-header {{
  width: 56%;
  text-align: center;
}}
.title-main {{
  font-size: 11.5pt;
  font-weight: bold;
  text-transform: uppercase;
}}
.author-title {{
  font-size: 10.5pt;
  font-style: italic;
  margin-top: 1px;
}}
.exam-title {{
  font-size: 11.5pt;
  font-weight: bold;
  line-height: 1.25;
  text-transform: uppercase;
}}
.subject-title {{
  font-size: 11.2pt;
  font-weight: bold;
  margin-top: 2px;
}}
.time-title {{
  font-size: 9.5pt;
  font-style: italic;
  margin-top: 1px;
}}
.left-box {{
  border: 1px solid #000;
  padding: 2px 6px;
  text-align: center;
  width: 175px;
  margin: 3px auto 0 auto;
  line-height: 1.22;
}}
.left-box .bold-text {{
  font-weight: bold;
  font-size: 10pt;
}}
.left-box .sub-text {{
  font-size: 9pt;
  font-style: italic;
  margin-top: 1px;
}}
.right-box {{
  border: 1.3px solid #000;
  padding: 2px 14px;
  font-weight: bold;
  font-size: 11pt;
  display: inline-block;
  margin-top: 2px;
}}
.solid-divider {{
  border-top: 1px solid #000;
  margin: 3px 0 1.5px 0;
}}
.solid-divider-thick {{
  border-top: 1.5px solid #000;
  margin: 2.5px 0 4px 0;
}}
.student-info {{
  display: flex;
  justify-content: space-between;
  font-size: 10pt;
  font-style: italic;
  margin-bottom: 2px;
}}
.section-title {{
  font-weight: bold;
  font-size: 10.5pt;
  margin-top: 3.5px;
  margin-bottom: 2px;
  text-align: justify;
}}
.section-subtitle {{
  font-style: italic;
  font-size: 9.5pt;
  margin-bottom: 2.5px;
}}
.question {{
  margin-bottom: 3.0px;
  text-align: justify;
  page-break-inside: avoid;
}}
.question-title {{
  font-weight: bold;
}}
.options-grid-4 {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 1.5px;
}}
.options-grid-2 {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  margin-top: 1.5px;
}}
.sub-item {{
  margin-left: 18px;
  margin-top: 1.5px;
  margin-bottom: 1.5px;
  line-height: 1.32;
  text-align: justify;
}}
.sub-item-label {{
  font-weight: bold;
}}
.end-exam {{
  text-align: center;
  margin-top: 6px;
  margin-bottom: 2px;
  font-weight: bold;
  font-size: 10.5pt;
}}
.end-note {{
  text-align: center;
  font-style: italic;
  font-size: 9.5pt;
}}
</style>
</head>
<body>

<!-- HEADER -->
<table class="header-table">
  <tr>
    <td class="left-header">
      <div class="title-main">ĐỀ ÔN TẬP CHÍNH THỨC</div>
      <div class="author-title">Biên soạn: Trần Trung Quân</div>
      <div class="left-box">
        <div class="bold-text">ĐỀ ÔN TẬP CHÍNH THỨC</div>
        <div class="sub-text">(Đề thi gồm có 03 trang)</div>
      </div>
    </td>
    <td class="right-header">
      <div class="exam-title">ĐỀ ÔN LUYỆN TỔNG HỢP</div>
      <div class="subject-title">Môn: TOÁN – Lớp 12</div>
      <div class="time-title">Thời gian làm bài: 90 phút, không kể thời gian giao đề</div>
      <div class="right-box">Mã đề: 113</div>
    </td>
  </tr>
</table>

<div class="solid-divider"></div>
<div class="student-info">
  <div>Họ và tên học sinh: ........................................................................................................</div>
  <div>Lớp: ...........................................</div>
</div>
<div class="solid-divider-thick"></div>

<!-- ==================== PHẦN I ==================== -->
<div class="section-title">PHẦN I. Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,25 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = \\dfrac{{2x - 3}}{{x + 1}}$. Mệnh đề nào dưới đây đúng?
  <div class="options-grid-2">
    <div><strong>A.</strong> Hàm số nghịch biến trên từng khoảng xác định.</div>
    <div><strong>B.</strong> Hàm số đồng biến trên $\\mathbb{{R}} \\setminus \\{{-1\\}}$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> Hàm số nghịch biến trên khoảng $(-\\infty; +\\infty)$.</div>
    <div><strong>D.</strong> Hàm số đồng biến trên mỗi khoảng $(-\\infty; -1)$ và $(-1; +\\infty)$.</div>
  </div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Giá trị nhỏ nhất của hàm số $f(x) = x^3 - 3x^2 + 2$ trên đoạn $[-1; 2]$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $-2$.</div>
    <div><strong>B.</strong> $2$.</div>
    <div><strong>C.</strong> $-4$.</div>
    <div><strong>D.</strong> $0$.</div>
  </div>
</div>

<!-- Câu 3 -->
<div class="question">
  <span class="question-title">Câu 3.</span> Trong không gian $Oxyz$, cho hai điểm $A(1; 2; -1)$ và $B(3; 0; 5)$. Tọa độ của vectơ $\\overrightarrow{{AB}}$ là
  <div class="options-grid-4">
    <div><strong>A.</strong> $(4; 2; 4)$.</div>
    <div><strong>B.</strong> $(2; 2; 6)$.</div>
    <div><strong>C.</strong> $(-2; 2; -6)$.</div>
    <div><strong>D.</strong> $(2; -2; 6)$.</div>
  </div>
</div>

<!-- Câu 4 -->
<div class="question">
  <span class="question-title">Câu 4.</span> Trong không gian $Oxyz$, cho hai vectơ $\\overrightarrow{{u}} = (2; -1; 1)$ và $\\overrightarrow{{v}} = (1; 3; -2)$. Tích vô hướng $\\overrightarrow{{u}} \\cdot \\overrightarrow{{v}}$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $3$.</div>
    <div><strong>B.</strong> $-3$.</div>
    <div><strong>C.</strong> $7$.</div>
    <div><strong>D.</strong> $-1$.</div>
  </div>
</div>

<!-- Câu 5 -->
<div class="question">
  <span class="question-title">Câu 5.</span> Họ tất cả các nguyên hàm của hàm số $f(x) = 4x^3 + \\cos x$ trên $\\mathbb{{R}}$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $x^4 - \\sin x + C$.</div>
    <div><strong>B.</strong> $12x^2 - \\sin x + C$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $x^4 + \\sin x + C$.</div>
    <div><strong>D.</strong> $12x^2 + \\sin x + C$.</div>
  </div>
</div>

<!-- Câu 6 -->
<div class="question">
  <span class="question-title">Câu 6.</span> Cho $\\int_{{0}}^{{3}} f(x)\\,\\mathrm{{d}}x = 4$ và $\\int_{{0}}^{{3}} g(x)\\,\\mathrm{{d}}x = -2$. Khi đó giá trị của $\\int_{{0}}^{{3}} [2f(x) - 3g(x)]\\,\\mathrm{{d}}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $2$.</div>
    <div><strong>B.</strong> $14$.</div>
    <div><strong>C.</strong> $8$.</div>
    <div><strong>D.</strong> $-2$.</div>
  </div>
</div>

<!-- Câu 7 -->
<div class="question">
  <span class="question-title">Câu 7.</span> Tích phân $\\int_{{0}}^{{1}} e^{{2x}}\\,\\mathrm{{d}}x$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $e^2 - 1$.</div>
    <div><strong>B.</strong> $2(e^2 - 1)$.</div>
    <div><strong>C.</strong> $\\dfrac{{e^2 + 1}}{{2}}$.</div>
    <div><strong>D.</strong> $\\dfrac{{e^2 - 1}}{{2}}$.</div>
  </div>
</div>

<!-- Câu 8 -->
<div class="question">
  <span class="question-title">Câu 8.</span> Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = 3x^2$, trục hoành $Ox$ và hai đường thẳng $x = 0, x = 2$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $6$.</div>
    <div><strong>B.</strong> $12$.</div>
    <div><strong>C.</strong> $8$.</div>
    <div><strong>D.</strong> $24$.</div>
  </div>
</div>

<!-- Câu 9 -->
<div class="question">
  <span class="question-title">Câu 9.</span> Trong không gian $Oxyz$, cho mặt cầu $(S): (x - 1)^2 + (y + 3)^2 + (z - 2)^2 = 16$. Tọa độ tâm $I$ và bán kính $R$ của mặt cầu $(S)$ lần lượt là
  <div class="options-grid-2">
    <div><strong>A.</strong> $I(1; -3; 2), R = 16$.</div>
    <div><strong>B.</strong> $I(-1; 3; -2), R = 4$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $I(1; -3; 2), R = 4$.</div>
    <div><strong>D.</strong> $I(-1; 3; -2), R = 16$.</div>
  </div>
</div>

<!-- Câu 10 -->
<div class="question">
  <span class="question-title">Câu 10.</span> Trong không gian $Oxyz$, mặt phẳng $(P)$ đi qua điểm $M(2; -1; 3)$ và nhận vectơ $\\overrightarrow{{n}} = (1; 3; -2)$ làm một vectơ pháp tuyến có phương trình là
  <div class="options-grid-2">
    <div><strong>A.</strong> $x + 3y - 2z + 7 = 0$.</div>
    <div><strong>B.</strong> $x + 3y - 2z - 7 = 0$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $2x - y + 3z + 7 = 0$.</div>
    <div><strong>D.</strong> $x + 3y - 2z + 5 = 0$.</div>
  </div>
</div>

<!-- Câu 11 -->
<div class="question">
  <span class="question-title">Câu 11.</span> Trong không gian $Oxyz$, phương trình chính tắc của đường thẳng $d$ đi qua điểm $A(1; -2; 4)$ và có một vectơ chỉ phương $\\overrightarrow{{u}} = (2; 5; -3)$ là
  <div class="options-grid-2">
    <div><strong>A.</strong> $\\dfrac{{x + 1}}{{2}} = \\dfrac{{y - 2}}{{5}} = \\dfrac{{z + 4}}{{-3}}$.</div>
    <div><strong>B.</strong> $\\dfrac{{x - 1}}{{2}} = \\dfrac{{y + 2}}{{5}} = \\dfrac{{z - 4}}{{-3}}$.</div>
  </div>
  <div class="options-grid-2">
    <div><strong>C.</strong> $\\dfrac{{x - 2}}{{1}} = \\dfrac{{y - 5}}{{-2}} = \\dfrac{{z + 3}}{{4}}$.</div>
    <div><strong>D.</strong> $\\dfrac{{x - 1}}{{2}} = \\dfrac{{y - 2}}{{5}} = \\dfrac{{z - 4}}{{-3}}$.</div>
  </div>
</div>

<!-- Câu 12 -->
<div class="question">
  <span class="question-title">Câu 12.</span> Trong không gian $Oxyz$, khoảng cách từ điểm $M(1; -2; 3)$ đến mặt phẳng $(P): 2x - 2y + z + 2 = 0$ bằng
  <div class="options-grid-4">
    <div><strong>A.</strong> $\\dfrac{{11}}{{3}}$.</div>
    <div><strong>B.</strong> $3$.</div>
    <div><strong>C.</strong> $\\dfrac{{7}}{{3}}$.</div>
    <div><strong>D.</strong> $\\dfrac{{11}}{{9}}$.</div>
  </div>
</div>

<!-- ==================== PHẦN II ==================== -->
<div style="page-break-before: always;"></div>
<div class="section-title" style="margin-top: 4px;">PHẦN II. Thí sinh trả lời từ câu 1 đến câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.</div>
<div class="section-subtitle">*(Điểm: đúng 1 ý được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng 4 ý được 1,0 điểm)*</div>

<!-- Câu 1 -->
<div class="question">
  <span class="question-title">Câu 1.</span> Cho hàm số $y = f(x) = \\dfrac{{x^2 - 3x + 3}}{{x - 1}}$ có đồ thị là $(C)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Hàm số đồng biến trên các khoảng $(-\\infty; 0)$ và $(2; +\\infty)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Đồ thị $(C)$ có đường tiệm cận đứng là $x = 1$ và đường tiệm cận xiên là $y = x - 2$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Tiếp tuyến của đồ thị $(C)$ tại điểm có hoành độ $x_0 = 0$ song song với trục hoành $Ox$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Tọa độ tâm đối xứng của đồ thị $(C)$ là giao điểm của hai đường tiệm cận $I(1; -1)$.</div>
</div>

<!-- Câu 2 -->
<div class="question">
  <span class="question-title">Câu 2.</span> Trong không gian với hệ tọa độ $Oxyz$, cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Cho biết tọa độ ba đỉnh đáy là $A(1; 0; 0)$, $B(2; 1; -1)$, $C(0; 3; 1)$ và đỉnh $S(1; 2; 4)$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Tọa độ đỉnh $D$ của hình bình hành đáy là $D(1; 2; 2)$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Tọa độ trọng tâm $G$ của tam giác $SAB$ là $G\\left(\\dfrac{{4}}{{3}}; 1; 1\\right)$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Thể tích của khối chóp $S.ABCD$ bằng $8$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Côsin của góc giữa hai vectơ $\\overrightarrow{{AB}}$ và $\\overrightarrow{{AD}}$ bằng $-\\dfrac{{\\sqrt{{6}}}}{{6}}$.</div>
</div>

<!-- Câu 3 -->
<div class="question" style="margin-bottom: 2px;">
  <span class="question-title">Câu 3.</span> Một chất điểm chuyển động theo quy luật vận tốc $v(t)\\text{{ (m/s)}}$ có đồ thị gồm các đoạn thẳng khi $0 \le t \le 3\\text{{ (s)}}$ và $8 \le t \le 15\\text{{ (s)}}$ và $v(t)$ có dạng đường parabol khi $3 \le t \le 8\\text{{ (s)}}$ (như hình vẽ bên dưới).
  <div style="text-align: center; margin: 1px 0;">{svg_kinematics}</div>
  Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Vận tốc của chất điểm đạt giá trị lớn nhất tại thời điểm $t = 8\\text{{ s}}$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Gia tốc của chất điểm tại thời điểm $t = 6\\text{{ s}}$ bằng $4\\text{{ m/s}}^2$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Quãng đường chất điểm đi được trong khoảng thời gian từ $8\\text{{ giây}}$ đến $15\\text{{ giây}}$ bằng $73,5\\text{{ m}}$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Vận tốc trung bình của chất điểm trong khoảng thời gian từ $0\\text{{ giây}}$ đến $15\\text{{ giây}}$ bằng $\dfrac{{869}}{{90}}\\text{{ m/s}}$.</div>
</div>

<!-- Câu 4 -->
<div class="question" style="margin-bottom: 5px;">
  <span class="question-title">Câu 4.</span> Trong không gian với hệ tọa độ $Oxyz$, cho mặt cầu $(S): x^2 + y^2 + z^2 - 2x + 4y - 4z - 7 = 0$ và mặt phẳng $(P): 2x + 2y - z + 10 = 0$. Xét tính đúng sai của các mệnh đề sau:
  <div class="sub-item"><span class="sub-item-label">a)</span> Mặt cầu $(S)$ có tâm $I(1; -2; 2)$ và bán kính $R = 4$.</div>
  <div class="sub-item"><span class="sub-item-label">b)</span> Khoảng cách từ tâm $I$ của mặt cầu $(S)$ đến mặt phẳng $(P)$ bằng $2$.</div>
  <div class="sub-item"><span class="sub-item-label">c)</span> Mặt phẳng $(P)$ cắt mặt cầu $(S)$ theo giao tuyến có chu vi bằng $4\\sqrt{{3}}\\pi$.</div>
  <div class="sub-item"><span class="sub-item-label">d)</span> Đường thẳng $\\Delta$ đi qua tâm $I$ và vuông góc với mặt phẳng $(P)$ có phương trình tham số là $\\begin{{cases}} x = 1 + 2t \\\\ y = -2 + 2t \\\\ z = 2 - t \\end{{cases}}$ ($t \\in \\mathbb{{R}}$).</div>
</div>

<div style="page-break-before: always;"></div>

<!-- ==================== PHẦN III (ĐẨY VÀO CUỐI TRANG 2) ==================== -->
<div class="section-title" style="margin-top: 5px;">PHẦN III. Thí sinh trả lời từ câu 1 đến câu 6.</div>
<div class="section-subtitle">*(Mỗi câu trả lời đúng thí sinh được 0,5 điểm)*</div>

<!-- Câu 1 có hình bên dưới -->
<div class="question" style="margin-bottom: 3px;">
  <span class="question-title">Câu 1.</span> Trên một bức tường thẳng đứng, người ta treo một tấm pano quảng cáo lớn có mép dưới cách mặt sàn $2,6\\text{{ m}}$ và mép trên cách mặt sàn $5,6\\text{{ m}}$. Một người quan sát có tầm mắt ở độ cao $1,6\\text{{ m}}$ so với mặt sàn nằm ngang trước bức tường (như hình vẽ bên dưới). Hỏi người đó phải đứng cách bức tường một khoảng bằng bao nhiêu mét để góc nhìn (góc trông) tấm pano quảng cáo theo phương thẳng đứng là lớn nhất?
  <div style="text-align: center; margin: 2px 0;">{svg_cau1}</div>
</div>

<!-- Câu 2 hình chóp đáy hình thang vuông -->
<div class="question" style="margin-top: 3px; margin-bottom: 3px;">
  <span class="question-title">Câu 2.</span> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang vuông tại $A$ và $B$, có đáy nhỏ $AD = a$, đáy lớn $BC = 2a$ và cạnh bên $AB = a$. Mặt bên $(SAB)$ là tam giác đều và nằm trong mặt phẳng vuông góc với mặt phẳng đáy $(ABCD)$. Tính số đo của góc giữa hai vectơ $\\overrightarrow{{SD}}$ và $\\overrightarrow{{BC}}$ theo đơn vị độ.
</div>

<!-- Câu 3 có hình ảnh bên dưới -->
<div class="question" style="margin-top: 3px; margin-bottom: 3px;">
  <span class="question-title">Câu 3.</span> Một cây cầu vòm bằng thép bắc qua một con kênh có vòm cầu dạng hình parabol. Khoảng cách giữa hai chân vòm cầu tại mặt nước là $24\\text{{ m}}$, điểm cao nhất của vòm cầu cách mặt nước $18\\text{{ m}}$. Mặt sàn cầu phẳng, nằm ngang và cách mặt nước $10\\text{{ m}}$. Người ta tiến hành sơn phản quang toàn bộ phần mặt bên của vòm cầu nằm phía trên mặt sàn cầu (như hình vẽ bên dưới). Biết chi phí sơn phản quang là $150.000\\text{{ đồng/m}}^2$. Hỏi tổng chi phí để sơn cả hai mặt bên (mặt trước và mặt sau) của phần vòm cầu đó bằng bao nhiêu triệu đồng?
  <div style="text-align: center; margin: 2px 0;">{svg_cau3}</div>
</div>

<!-- Câu 4 thể tích vật thể -->
<div class="question" style="margin-bottom: 5px;">
  <span class="question-title">Câu 4.</span> Một khối đá phong thủy trang trí có mặt đáy nằm trên mặt đất là một hình tròn có bán kính $R = 3\\text{{ dm}}$. Khi cắt khối đá bởi các mặt phẳng song song với nhau và vuông góc với mặt phẳng đáy, thiết diện thu được luôn là một hình vuông có một cạnh nằm trên mặt đáy. Tính thể tích của khối đá phong thủy đó theo đơn vị $\\text{{dm}}^3$.
</div>

<!-- Câu 5 Heron 3D -->
<div class="question" style="margin-bottom: 5px;">
  <span class="question-title">Câu 5.</span> Trong không gian với hệ tọa độ $Oxyz$ (đơn vị đo trên các trục tọa độ là kilômét), hai trạm thu phát tín hiệu mặt đất được đặt tại hai vị trí $A(5; 2; 5)$ và $B(5; 8; 8)$. Một tuyến cáp quang chính được chôn ngầm trong mặt phẳng $(\\alpha): 2x - y + 2z - 9 = 0$. Người ta cần đặt một trạm chuyển tiếp $M$ trên mặt phẳng $(\\alpha)$ và kéo hai đường cáp nhánh từ $M$ đến $A$ và từ $M$ đến $B$ sao cho tổng chiều dài cáp nhánh $MA + MB$ là ngắn nhất. Tổng chiều dài ngắn nhất của hai đường cáp nhánh đó bằng bao nhiêu kilômét?
</div>

<!-- Câu 6 thiết diện mặt cầu -->
<div class="question" style="margin-bottom: 8px;">
  <span class="question-title">Câu 6.</span> Trong không gian với hệ tọa độ $Oxyz$, cho mặt cầu $(S): (x - 3)^2 + (y + 2)^2 + z^2 = 25$ và đường thẳng $d: \\dfrac{{x - 1}}{{1}} = \\dfrac{{y}}{{2}} = \\dfrac{{z + 1}}{{2}}$. Mặt phẳng $(P)$ thay đổi nhưng luôn chứa đường thẳng $d$ và cắt mặt cầu $(S)$ theo giao tuyến là một đường tròn $(C)$. Bán kính của đường tròn $(C)$ đạt giá trị nhỏ nhất bằng bao nhiêu?
</div>

<div class="end-exam">---------- HẾT ----------</div>
<div class="end-note">Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.</div>

<script>
document.addEventListener("DOMContentLoaded", function() {{
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "$$", right: "$$", display: true}},
      {{left: "$", right: "$", display: false}}
    ],
    throwOnError: false
  }});
}});
</script>
</body>
</html>
"""

html_filename = 'exam_de_khao_sat_toan_12_ma113.html'
pdf_name = "De_Thi_Khao_Sat_Toan_12_Ma_113.pdf"

with open(html_filename, 'w', encoding='utf-8') as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_name}",
    html_filename
]

print("Running Chrome to generate De 113 PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

reader = pypdf.PdfReader(pdf_name)
print(f"Total pages: {len(reader.pages)}")
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    print(f"Page {i+1} lines: {len(txt.splitlines())}")
