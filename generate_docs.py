import os

docs = {
    "tomato_bacterial_spot.md": """# Tomato Bacterial Spot (Xanthomonas campestris pv. vesicatoria)

## Causal Organism
Bacteria (*Xanthomonas campestris pv. vesicatoria*). Highly active in warm, humid weather with frequent rainfall.

## Symptoms
Small, water-soaked spots on leaves that turn brown/black with a yellow halo. Fruit develops dark, raised, scab-like lesions. Leaves may turn yellow and drop prematurely.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Copper Oxychloride 50% WP (Trade names: Blitox, Blue Copper)**
   - **Dosage:** 2.5 to 3.0 g per liter of water.
   - **Action:** Broad-spectrum contact bactericide/fungicide.
2. **Streptomycin Sulphate 9% + Tetracycline Hydrochloride 1% SP (Trade name: Streptocycline)**
   - **Dosage:** 0.1 g to 0.2 g per liter of water (often tank-mixed with Copper Oxychloride).
   - **Action:** Antibiotic specifically targeting bacterial cell division.

## Organic Alternatives
- **Pseudomonas fluorescens (1% WP):** 5-10 g per liter of water as a foliar spray.
- **Copper Hydroxide 77% WP (Kocide):** 2 g per liter (approved in some organic regimens).

## Spray Timing Rules
- **Weather Dependency:** Do NOT spray if heavy rain is expected within 4 hours. Spray during early morning (6 AM - 9 AM) or late afternoon (4 PM - 6 PM) to avoid phytotoxicity from copper under high sun.
- **Frequency:** Reapply every 7-10 days if humid/rainy weather persists.

## Resistance Management
Do not rely solely on Streptocycline. Always tank-mix antibiotics with a copper-based protectant. Limit antibiotic sprays to a maximum of 2-3 per season to prevent resistant bacterial strains.

## Cost Estimate (INR/Acre)
- Copper Oxychloride: ₹400 - ₹600
- Streptocycline: ₹150 - ₹250
- **Total Estimated Cost/Acre/Spray:** ₹550 - ₹850
""",

    "tomato_early_blight.md": """# Tomato Early Blight (Alternaria solani)

## Causal Organism
Fungus (*Alternaria solani*). Favored by warm temperatures (24-29°C) and heavy dew or frequent rain.

## Symptoms
Target-like, concentric dark rings on older lower leaves. Surrounding tissue turns yellow. Stem lesions and fruit rot at the stem end can also occur. Defoliation exposes fruit to sunscald.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Mancozeb 75% WP (Trade names: Dithane M-45, Indofil M-45)**
   - **Dosage:** 2.0 to 2.5 g per liter of water.
   - **Action:** Contact protectant fungicide.
2. **Azoxystrobin 23% SC (Trade name: Amistar)**
   - **Dosage:** 1.0 ml per liter of water.
   - **Action:** Systemic curative and protectant (Strobilurin class).
3. **Tebuconazole 50% + Trifloxystrobin 25% WG (Trade name: Nativo)**
   - **Dosage:** 0.7 g per liter of water.
   - **Action:** Broad-spectrum systemic combination.

## Organic Alternatives
- **Bacillus subtilis:** 5-10 ml/g per liter of water.
- **Neem Oil (1500 ppm):** 3-5 ml per liter of water (acts primarily as a preventive).

## Spray Timing Rules
- **Weather Dependency:** Apply preventatively before forecasted extended wet periods. Do not apply Azoxystrobin during extreme heat (>35°C) to avoid leaf burn.
- **Frequency:** 10-14 day intervals. Reduce to 7 days during highly favorable weather.

## Resistance Management
Strict rotation is required for Strobilurins (Azoxystrobin). Never apply Azoxystrobin or Nativo for more than 2 consecutive sprays. Alternate with a multi-site contact fungicide like Mancozeb or Chlorothalonil.

## Cost Estimate (INR/Acre)
- Mancozeb: ₹300 - ₹450
- Azoxystrobin/Nativo: ₹800 - ₹1,200
- **Total Estimated Cost/Acre/Spray:** ₹300 - ₹1,200 (depending on chemical choice)
""",

    "tomato_late_blight.md": """# Tomato Late Blight (Phytophthora infestans)

## Causal Organism
Oomycete water mold (*Phytophthora infestans*). Extremely destructive in cool, wet weather (15-20°C with high relative humidity >90%).

## Symptoms
Large, irregular, water-soaked, greasy-looking patches on leaves. White powdery fungal growth on the underside of leaves during high humidity. Dark brown, firm lesions on fruit. Can destroy a field in days.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Metalaxyl 8% + Mancozeb 64% WP (Trade names: Ridomil Gold, Krilaxyl)**
   - **Dosage:** 2.0 to 2.5 g per liter of water.
   - **Action:** Systemic (Metalaxyl) and contact (Mancozeb) eradication.
2. **Cymoxanil 8% + Mancozeb 64% WP (Trade name: Curzate M8)**
   - **Dosage:** 3.0 g per liter of water.
   - **Action:** Penetrant with kick-back curative action.
3. **Dimethomorph 50% WP (Trade name: Acrobat)**
   - **Dosage:** 1.0 to 1.5 g per liter of water (must be tank-mixed with Mancozeb).

## Organic Alternatives
- **Copper Hydroxide 77% WP:** 2 g per liter (preventative only).
- **Trichoderma viride:** Applied to soil and foliage, but largely ineffective once a severe outbreak begins.

## Spray Timing Rules
- **Weather Dependency:** High urgency. If night temperatures are below 20°C with heavy dew/fog/rain, spray immediately. Ensure thoroughly dried canopy before rain hits (requires 2 hours rain-free post-spray).
- **Frequency:** 5-7 days under severe pressure. 

## Resistance Management
*Phytophthora* develops resistance to Metalaxyl very quickly. Do not use Metalaxyl products if resistance is known in your region. Always alternate Metalaxyl/Cymoxanil with Dimethomorph or purely contact fungicides (Chlorothalonil).

## Cost Estimate (INR/Acre)
- Ridomil Gold / Curzate: ₹900 - ₹1,400
- **Total Estimated Cost/Acre/Spray:** ₹1,000 - ₹1,500
""",

    "tomato_leaf_mold.md": """# Tomato Leaf Mold (Passalora fulva)

## Causal Organism
Fungus (*Passalora fulva*, formerly *Fulvia fulva*). Highly prevalent in polyhouses, greenhouses, or extremely humid environments with poor air circulation.

## Symptoms
Pale green to yellow spots on the upper leaf surface. The underside of the spots develops an olive-green to gray velvety fungal growth. Infected leaves eventually turn yellow, wither, and drop.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Difenoconazole 25% EC (Trade name: Score)**
   - **Dosage:** 0.5 to 1.0 ml per liter of water.
   - **Action:** Systemic triazole fungicide.
2. **Chlorothalonil 75% WP (Trade name: Kavach)**
   - **Dosage:** 2.0 g per liter of water.
   - **Action:** Broad-spectrum contact protectant.

## Organic Alternatives
- **Baking Soda (Sodium Bicarbonate):** 1 tsp per liter of water with a few drops of mild soap (alters leaf pH to prevent fungal spore germination).
- **Neem Extract (Azadirachtin 10000 ppm):** 2 ml per liter.

## Spray Timing Rules
- **Weather Dependency:** Spray when relative humidity exceeds 85%. Best sprayed in the morning so leaves dry quickly.
- **Cultural Rule:** Prune lower leaves to improve ventilation before spraying.

## Resistance Management
Alternate Difenoconazole (Group 3) with Chlorothalonil (Group M5). Ensure proper pruning; chemicals alone cannot solve leaf mold in a dense, unventilated canopy.

## Cost Estimate (INR/Acre)
- Difenoconazole: ₹600 - ₹800
- Chlorothalonil: ₹450 - ₹600
- **Total Estimated Cost/Acre/Spray:** ₹500 - ₹800
""",

    "tomato_septoria_leaf_spot.md": """# Tomato Septoria Leaf Spot (Septoria lycopersici)

## Causal Organism
Fungus (*Septoria lycopersici*). Spreads rapidly via splashing rain and overhead irrigation.

## Symptoms
Numerous small, circular spots (1/16 to 1/8 inch) with dark brown margins and tan/gray centers. Tiny black dots (pycnidia) can often be seen in the center of the spots. Heavily infected leaves turn yellow and drop off.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Propiconazole 25% EC (Trade name: Tilt)**
   - **Dosage:** 1.0 ml per liter of water.
   - **Action:** Systemic curative fungicide.
2. **Mancozeb 75% WP (Trade names: Dithane M-45)**
   - **Dosage:** 2.5 g per liter of water.
   - **Action:** Contact protectant.

## Organic Alternatives
- **Copper Oxychloride 50% WP:** 2.5 g per liter.
- **Trichoderma harzianum:** 5 g per liter (preventative foliar application).

## Spray Timing Rules
- **Weather Dependency:** Apply immediately after heavy rains that cause soil splashing. Do not use overhead sprinklers while fighting this disease.
- **Frequency:** Every 7-10 days until symptoms halt.

## Resistance Management
Alternate between systemic (Propiconazole) and contact (Mancozeb) to prevent resistance build-up. Always apply a thick layer of organic mulch at the base of the plant to prevent fungal spores in the soil from splashing onto lower leaves.

## Cost Estimate (INR/Acre)
- Propiconazole: ₹500 - ₹700
- Mancozeb: ₹300 - ₹450
- **Total Estimated Cost/Acre/Spray:** ₹400 - ₹700
""",

    "tomato_spider_mite.md": """# Tomato Two-Spotted Spider Mite (Tetranychus urticae)

## Causal Organism
Arachnid (*Tetranychus urticae*). Explodes in population during hot, dry, dusty weather.

## Symptoms
Tiny, yellowish or whitish stippling/specks on leaves. Fine, silky webbing on the underside of leaves and stems. Severe infestations cause leaves to turn completely yellow, dry out, and die.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Spiromesifen 22.9% SC (Trade name: Oberon)**
   - **Dosage:** 1.0 ml per liter of water.
   - **Action:** Inhibits lipid biosynthesis, highly effective on eggs and nymphs.
2. **Abamectin 1.9% EC (Trade name: Vertimec, Bhasma)**
   - **Dosage:** 0.5 to 1.0 ml per liter of water.
   - **Action:** Translaminar acaricide/insecticide.
3. **Propargite 57% EC (Trade name: Omite)**
   - **Dosage:** 2.0 ml per liter of water.

## Organic Alternatives
- **Horticultural Oil / Neem Oil (10000 ppm):** 3-5 ml per liter of water (suffocates mites).
- **Wettable Sulfur 80% WDG:** 2-3 g per liter (Do not use when temperature >30°C).

## Spray Timing Rules
- **Weather Dependency:** NEVER spray Sulfur or Oils when temperatures exceed 32°C (causes severe burning). Ensure total underside leaf coverage, as mites live underneath the leaves.
- **Frequency:** Spray exactly 5-7 days after the first spray to kill newly hatched eggs (acaricides often don't kill all life stages).

## Resistance Management
Spider mites develop resistance incredibly fast (sometimes within one season). NEVER use the same chemical class twice in a row. Rotate Spiromesifen (Group 23) -> Abamectin (Group 6) -> Propargite (Group 12C).

## Cost Estimate (INR/Acre)
- Spiromesifen (Oberon): ₹1,200 - ₹1,600
- Abamectin: ₹800 - ₹1,000
- **Total Estimated Cost/Acre/Spray:** ₹1,000 - ₹1,600
""",

    "tomato_target_spot.md": """# Tomato Target Spot (Corynespora cassiicola)

## Causal Organism
Fungus (*Corynespora cassiicola*). Thrives in warm temperatures (20-28°C) with high humidity and prolonged leaf wetness.

## Symptoms
Lesions on leaves start as small brown spots and expand into large, circular spots with concentric rings (similar to early blight, but spots are usually larger and paler). Causes rapid defoliation. Can also cause sunken, dark lesions on fruit.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Tebuconazole 50% + Trifloxystrobin 25% WG (Trade name: Nativo)**
   - **Dosage:** 0.7 g per liter of water.
   - **Action:** Systemic and translaminar broad-spectrum control.
2. **Metiram 55% + Pyraclostrobin 5% WG (Trade name: Cabrio Top)**
   - **Dosage:** 3.0 g per liter of water.
   - **Action:** Multi-site contact and systemic.

## Organic Alternatives
- **Bacillus subtilis:** Preventative sprays at 5 g/ml per liter.
- **Copper Oxychloride 50% WP:** 2.5 g per liter (preventative).

## Spray Timing Rules
- **Weather Dependency:** Apply prior to forecasted periods of heavy rainfall and high humidity. Ensure canopy is dry before applying.
- **Frequency:** 10-14 days.

## Resistance Management
Do not make more than two sequential applications of Group 11 (Strobilurin) fungicides like Pyraclostrobin or Trifloxystrobin. Rotate with Group M protectants like Mancozeb or Chlorothalonil.

## Cost Estimate (INR/Acre)
- Nativo / Cabrio Top: ₹1,000 - ₹1,500
- **Total Estimated Cost/Acre/Spray:** ₹1,000 - ₹1,500
""",

    "tomato_yellow_leaf_curl_virus.md": """# Tomato Yellow Leaf Curl Virus (TYLCV)

## Causal Organism
Begomovirus, transmitted exclusively by the Whitefly (*Bemisia tabaci*). The virus itself cannot be killed by chemicals; control relies entirely on killing the vector (whiteflies).

## Symptoms
Severe stunting of the plant. New leaves are significantly reduced in size, curl upward, and become yellow (chlorotic) between the veins. Flowers drop, and fruit production completely halts.

## CIB&RC Registered Pesticides (Vector Control - Whiteflies)
1. **Imidacloprid 17.8% SL (Trade names: Confidor, Tata Mida)**
   - **Dosage:** 0.3 to 0.5 ml per liter of water.
   - **Action:** Systemic neonicotinoid targeting sap-sucking insects.
2. **Diafenthiuron 50% WP (Trade name: Pegasus)**
   - **Dosage:** 1.0 to 1.5 g per liter of water.
   - **Action:** Contact and stomach poison with translaminar action.
3. **Flonicamid 50% WG (Trade name: Ulala)**
   - **Dosage:** 0.3 g per liter of water.

## Organic Alternatives
- **Yellow Sticky Traps:** Install 15-20 traps per acre to catch adult whiteflies.
- **Neem Oil (10000 ppm):** 3-5 ml per liter (acts as a strong feeding deterrent and disrupts mating).
- **Verticillium lecanii (Bio-insecticide):** 5 g per liter.

## Spray Timing Rules
- **Weather Dependency:** Whiteflies are most active during warm, dry periods. Spray early morning when whiteflies are sluggish.
- **Action Threshold:** Uproot and burn infected plants immediately. Spray the surrounding healthy plants.

## Resistance Management
Rotate chemical classes. Do not use Imidacloprid (Neonicotinoid) repeatedly. Rotate with Diafenthiuron or Flonicamid. Overuse of Neonicotinoids can also trigger spider mite outbreaks.

## Cost Estimate (INR/Acre)
- Imidacloprid: ₹200 - ₹350
- Flonicamid / Pegasus: ₹700 - ₹1,200
- **Total Estimated Cost/Acre/Spray:** ₹300 - ₹1,000
""",

    "tomato_mosaic_virus.md": """# Tomato Mosaic Virus (ToMV)

## Causal Organism
Tobamovirus. Highly contagious via mechanical transmission (hands, tools, clothing, rubbing leaves). Can survive in soil and seed coats.

## Symptoms
Leaves show a distinct light and dark green mottled or mosaic pattern. Leaves may be stunted, crinkled, or fern-like. Fruit maturation is delayed, and yields are severely reduced.

## CIB&RC Registered Pesticides
**NONE.** There are no chemical cures for viral infections in plants.

## Actionable Management Steps
1. **Immediate Rogueing:** Pull out the infected plant(s) immediately by the roots. Place them in a plastic bag to avoid brushing against healthy plants. Burn or deeply bury the infected plants (do NOT compost).
2. **Sanitation:** Wash hands thoroughly with soap and water after handling any tomato plants. Disinfect all pruning tools with a 10% bleach solution or 70% alcohol between every single plant.
3. **Avoid Tobacco:** Tobamoviruses are related to Tobacco Mosaic Virus. Workers should not smoke or chew tobacco near the fields, and must wash hands after using tobacco products before touching plants.
4. **Seed Treatment (For Next Season):** Soak seeds in a 10% Trisodium Phosphate (TSP) solution for 15 minutes before sowing.

## Spray Timing Rules
- **N/A.** Do not waste money spraying fungicides or insecticides, as they will not cure a virus.

## Resistance Management
Purchase certified virus-free seeds and specifically look for ToMV-resistant tomato varieties (indicated by "Tm" or "ToMV" on the seed packet) for future plantings.

## Cost Estimate (INR/Acre)
- **Chemical Cost:** ₹0
- **Labor Cost:** Variable (cost of rogueing and sanitation).
""",

    "potato_late_blight.md": """# Potato Late Blight (Phytophthora infestans)

## Causal Organism
Oomycete (*Phytophthora infestans*). The same devastating pathogen that causes Tomato Late Blight. Historically responsible for the Irish Potato Famine.

## Symptoms
Water-soaked, dark green to black lesions on leaves, often starting at the tips or edges. In high humidity, a white, fluffy fungal growth appears on the undersides of the lesions. Tubers develop shallow, reddish-brown, dry, granular rot under the skin.

## CIB&RC Registered Pesticides (Chemical Control)
1. **Cymoxanil 8% + Mancozeb 64% WP (Trade name: Curzate M8, Moximate)**
   - **Dosage:** 3.0 g per liter of water.
   - **Action:** Curative penetrant and contact protectant.
2. **Dimethomorph 50% WP (Trade name: Acrobat)**
   - **Dosage:** 1.0 to 1.5 g per liter of water.
   - **Action:** Anti-sporulant (stops disease spread).
3. **Mancozeb 75% WP (Trade name: Dithane M-45)**
   - **Dosage:** 2.5 g per liter of water.
   - **Action:** Preventative contact only.

## Organic Alternatives
- **Copper Oxychloride 50% WP:** 2.5 g per liter (strictly preventative).
- **Avoid Excess Nitrogen:** High nitrogen promotes lush, dense foliage which restricts airflow and favors blight.

## Spray Timing Rules
- **Weather Dependency:** Monitor weather closely. If temperatures drop to 12-18°C combined with heavy fog, dew, or rain, spray Mancozeb preventatively. If symptoms are seen, switch immediately to Cymoxanil + Mancozeb.
- **Harvesting:** Do not harvest tubers when the soil is wet or if vines are still green and infected. Kill vines chemically or mechanically 2 weeks before harvest to allow skins to set and prevent tuber infection.

## Resistance Management
Strict rotation is essential. *Phytophthora infestans* adapts quickly. Do not use systemic fungicides (like Metalaxyl or Dimethomorph) for more than 2 consecutive sprays. Always ensure a contact fungicide is included in the mix.

## Cost Estimate (INR/Acre)
- Cymoxanil+Mancozeb: ₹1,000 - ₹1,400
- **Total Estimated Cost/Acre/Spray:** ₹1,000 - ₹1,500
"""
}

for filename, content in docs.items():
    path = os.path.join("backend", "rag", "advisory_docs", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Created 10 RAG markdown files successfully!")
