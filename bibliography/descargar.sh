#!/usr/bin/env bash
# Descarga la bibliografía de libre acceso del curso a bibliography/papers/.
# Los PDFs NO se versionan en el repo (es público y varios tienen copyright):
# cada uno los baja localmente para uso personal/de estudio.
# Uso: bash bibliography/descargar.sh   (desde la raíz del repo)
set -u
DEST="$(dirname "$0")/papers"
mkdir -p "$DEST"
bajar() {  # bajar <archivo> <url> <pausa_seg>
  if [ -s "$DEST/$1" ]; then echo "ya existe  $1"; return; fi
  if curl -sSfL -m 180 -A "Mozilla/5.0 (curso ITBA)" -o "$DEST/$1.tmp" "$2" \
     && [ "$(head -c 4 "$DEST/$1.tmp")" = "%PDF" ]; then   # descarta páginas HTML (anti-bots, logins)
    mv "$DEST/$1.tmp" "$DEST/$1"; echo "OK         $1"
  else
    rm -f "$DEST/$1.tmp"; echo "FALLÓ      $1  <- $2"
  fi
  sleep "$3"
}

# --- Papers de arXiv (pausa de 3 s entre descargas, según la política de uso de arXiv) ---
bajar "2022_yao_2210.03629.pdf" "https://arxiv.org/pdf/2210.03629" 3
bajar "2023_schick_2302.04761.pdf" "https://arxiv.org/pdf/2302.04761" 3
bajar "2023_patil_2305.15334.pdf" "https://arxiv.org/pdf/2305.15334" 3
bajar "2023_shinn_2303.11366.pdf" "https://arxiv.org/pdf/2303.11366" 3
bajar "2023_wang_2308.11432.pdf" "https://arxiv.org/pdf/2308.11432" 3
bajar "2024_yao_2406.12045.pdf" "https://arxiv.org/pdf/2406.12045" 3
bajar "2023_es_2309.15217.pdf" "https://arxiv.org/pdf/2309.15217" 3
bajar "2023_saad-falcon_2311.09476.pdf" "https://arxiv.org/pdf/2311.09476" 3
bajar "2023_zheng_2306.05685.pdf" "https://arxiv.org/pdf/2306.05685" 3
bajar "2023_wang_2305.17926.pdf" "https://arxiv.org/pdf/2305.17926" 3
bajar "2023_liu_2303.16634.pdf" "https://arxiv.org/pdf/2303.16634" 3
bajar "2024_panickssery_2404.13076.pdf" "https://arxiv.org/pdf/2404.13076" 3
bajar "2019_nogueira_1901.04085.pdf" "https://arxiv.org/pdf/1901.04085" 3
bajar "2020_khattab_2004.12832.pdf" "https://arxiv.org/pdf/2004.12832" 3
bajar "2021_thakur_2104.08663.pdf" "https://arxiv.org/pdf/2104.08663" 3
bajar "2022_gao_2212.10496.pdf" "https://arxiv.org/pdf/2212.10496" 3
bajar "2023_ma_2305.14283.pdf" "https://arxiv.org/pdf/2305.14283" 3
bajar "2024_rackauckas_2402.03367.pdf" "https://arxiv.org/pdf/2402.03367" 3
bajar "2024_sarthi_2401.18059.pdf" "https://arxiv.org/pdf/2401.18059" 3
bajar "2024_edge_2404.16130.pdf" "https://arxiv.org/pdf/2404.16130" 3
bajar "2023_asai_2310.11511.pdf" "https://arxiv.org/pdf/2310.11511" 3
bajar "2024_yan_2401.15884.pdf" "https://arxiv.org/pdf/2401.15884" 3
bajar "2023_jiang_2310.05736.pdf" "https://arxiv.org/pdf/2310.05736" 3
bajar "2023_xu_2310.04408.pdf" "https://arxiv.org/pdf/2310.04408" 3
bajar "2023_liu_2307.03172.pdf" "https://arxiv.org/pdf/2307.03172" 3
bajar "2024_barnett_2401.05856.pdf" "https://arxiv.org/pdf/2401.05856" 3
bajar "2020_hogan_2003.02320.pdf" "https://arxiv.org/pdf/2003.02320" 3
bajar "2023_gao_2312.10997.pdf" "https://arxiv.org/pdf/2312.10997" 3
bajar "2023_zheng_2310.06117.pdf" "https://arxiv.org/pdf/2310.06117" 3
bajar "2020_lewis_2005.11401.pdf" "https://arxiv.org/pdf/2005.11401" 3
bajar "2020_guu_2002.08909.pdf" "https://arxiv.org/pdf/2002.08909" 3
bajar "2020_karpukhin_2004.04906.pdf" "https://arxiv.org/pdf/2004.04906" 3
bajar "2021_borgeaud_2112.04426.pdf" "https://arxiv.org/pdf/2112.04426" 3
bajar "2020_izacard_2007.01282.pdf" "https://arxiv.org/pdf/2007.01282" 3
bajar "2023_gao_2305.14627.pdf" "https://arxiv.org/pdf/2305.14627" 3
bajar "2023_huang_2311.05232.pdf" "https://arxiv.org/pdf/2311.05232" 3
bajar "2023_shi_2302.00093.pdf" "https://arxiv.org/pdf/2302.00093" 3
bajar "2023_greshake_2302.12173.pdf" "https://arxiv.org/pdf/2302.12173" 3
bajar "2016_malkov_1603.09320.pdf" "https://arxiv.org/pdf/1603.09320" 3
bajar "2017_johnson_1702.08734.pdf" "https://arxiv.org/pdf/1702.08734" 3
bajar "2024_douze_2401.08281.pdf" "https://arxiv.org/pdf/2401.08281" 3
bajar "2018_aumuller_1807.05614.pdf" "https://arxiv.org/pdf/1807.05614" 3
bajar "2022_muennighoff_2210.07316.pdf" "https://arxiv.org/pdf/2210.07316" 3
bajar "2013_mikolov_1301.3781.pdf" "https://arxiv.org/pdf/1301.3781" 3
bajar "2019_reimers_1908.10084.pdf" "https://arxiv.org/pdf/1908.10084" 3
bajar "2018_oord_1807.03748.pdf" "https://arxiv.org/pdf/1807.03748" 3
bajar "2021_gao_2104.08821.pdf" "https://arxiv.org/pdf/2104.08821" 3
bajar "2021_izacard_2112.09118.pdf" "https://arxiv.org/pdf/2112.09118" 3
bajar "2022_kusupati_2205.13147.pdf" "https://arxiv.org/pdf/2205.13147" 3
bajar "2024_gunther_2409.04701.pdf" "https://arxiv.org/pdf/2409.04701" 3
bajar "2019_ethayarajh_1909.00512.pdf" "https://arxiv.org/pdf/1909.00512" 3
bajar "2022_wang_2212.03533.pdf" "https://arxiv.org/pdf/2212.03533" 3
bajar "2023_willard_2307.09702.pdf" "https://arxiv.org/pdf/2307.09702" 3
bajar "2024_tam_2408.02442.pdf" "https://arxiv.org/pdf/2408.02442" 3
bajar "2023_geng_2305.13971.pdf" "https://arxiv.org/pdf/2305.13971" 3
bajar "2020_brown_2005.14165.pdf" "https://arxiv.org/pdf/2005.14165" 3
bajar "2022_min_2202.12837.pdf" "https://arxiv.org/pdf/2202.12837" 3
bajar "2022_wei_2201.11903.pdf" "https://arxiv.org/pdf/2201.11903" 3
bajar "2022_kojima_2205.11916.pdf" "https://arxiv.org/pdf/2205.11916" 3
bajar "2024_schulhoff_2406.06608.pdf" "https://arxiv.org/pdf/2406.06608" 3
bajar "2022_ouyang_2203.02155.pdf" "https://arxiv.org/pdf/2203.02155" 3
bajar "2019_holtzman_1904.09751.pdf" "https://arxiv.org/pdf/1904.09751" 3
bajar "2022_perez_2211.09527.pdf" "https://arxiv.org/pdf/2211.09527" 3
bajar "2021_zhao_2102.09690.pdf" "https://arxiv.org/pdf/2102.09690" 3
bajar "2021_lu_2104.08786.pdf" "https://arxiv.org/pdf/2104.08786" 3
bajar "2017_vaswani_1706.03762.pdf" "https://arxiv.org/pdf/1706.03762" 3
bajar "2015_sennrich_1508.07909.pdf" "https://arxiv.org/pdf/1508.07909" 3
bajar "2014_bahdanau_1409.0473.pdf" "https://arxiv.org/pdf/1409.0473" 3
bajar "2020_kaplan_2001.08361.pdf" "https://arxiv.org/pdf/2001.08361" 3
bajar "2022_hoffmann_2203.15556.pdf" "https://arxiv.org/pdf/2203.15556" 3
bajar "2021_bommasani_2108.07258.pdf" "https://arxiv.org/pdf/2108.07258" 3
bajar "2023_touvron_2307.09288.pdf" "https://arxiv.org/pdf/2307.09288" 3
bajar "2023_petrov_2305.15425.pdf" "https://arxiv.org/pdf/2305.15425" 3

# --- Libros y papers de acceso abierto fuera de arXiv ---
bajar "2009_robertson_bm25-probabilistic-relevance-framework.pdf" "https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf" 1
bajar "2009_cormack_reciprocal-rank-fusion.pdf" "https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf" 1
bajar "2003_bengio_neural-probabilistic-language-model.pdf" "https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf" 1
bajar "2019_radford_gpt2-language-models-unsupervised-multitask.pdf" "https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf" 1
bajar "2025_jurafsky-martin_speech-and-language-processing-3ed.pdf" "https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf" 1
bajar "2008_manning_introduction-to-information-retrieval.pdf" "https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf" 1

# --- Clases 1 a 6: fuentes agregadas en los apuntes ---
bajar "2017_geifman_1705.08500.pdf" "https://arxiv.org/pdf/1705.08500" 3
bajar "2018_devlin_1810.04805.pdf" "https://arxiv.org/pdf/1810.04805" 3
bajar "2018_fan_1805.04833.pdf" "https://arxiv.org/pdf/1805.04833" 3
bajar "2018_kudo_1808.06226.pdf" "https://arxiv.org/pdf/1808.06226" 3
bajar "2019_petroni_1909.01066.pdf" "https://arxiv.org/pdf/1909.01066" 3
bajar "2020_wang_2005.10242.pdf" "https://arxiv.org/pdf/2005.10242" 3
bajar "2021_rashkin_2112.12870.pdf" "https://arxiv.org/pdf/2112.12870" 3
bajar "2021_su_2104.09864.pdf" "https://arxiv.org/pdf/2104.09864" 3
bajar "2022_kadavath_2207.05221.pdf" "https://arxiv.org/pdf/2207.05221" 3
bajar "2022_mallen_2212.10511.pdf" "https://arxiv.org/pdf/2212.10511" 3
bajar "2022_pope_2211.05102.pdf" "https://arxiv.org/pdf/2211.05102" 3
bajar "2023_kwon_2309.06180.pdf" "https://arxiv.org/pdf/2309.06180" 3
bajar "2023_pan_2310.14021.pdf" "https://arxiv.org/pdf/2310.14021" 3
bajar "2023_ram_2302.00083.pdf" "https://arxiv.org/pdf/2302.00083" 3
bajar "2023_sclar_2310.11324.pdf" "https://arxiv.org/pdf/2310.11324" 3
bajar "2024_patel_2403.04871.pdf" "https://arxiv.org/pdf/2403.04871" 3
bajar "2024_wallace_2404.13208.pdf" "https://arxiv.org/pdf/2404.13208" 3

# --- Clase 10: LangGraph, human-in-the-loop y MCP ---
bajar "2025_feng_2506.12469.pdf" "https://arxiv.org/pdf/2506.12469" 3
bajar "2025_mitchell_2502.02649.pdf" "https://arxiv.org/pdf/2502.02649" 3
bajar "2025_beurer-kellner_2506.08837.pdf" "https://arxiv.org/pdf/2506.08837" 3
bajar "2025_hou_2503.23278.pdf" "https://arxiv.org/pdf/2503.23278" 3
bajar "2025_radosevich_2504.03767.pdf" "https://arxiv.org/pdf/2504.03767" 3
bajar "2025_debenedetti_2503.18813.pdf" "https://arxiv.org/pdf/2503.18813" 3
bajar "2023_wu_2308.08155.pdf" "https://arxiv.org/pdf/2308.08155" 3
bajar "2025_cemri_2503.13657.pdf" "https://arxiv.org/pdf/2503.13657" 3
bajar "2023_sumers_2309.02427.pdf" "https://arxiv.org/pdf/2309.02427" 3
bajar "2023_packer_2310.08560.pdf" "https://arxiv.org/pdf/2310.08560" 3
bajar "2023_xu_2305.18323.pdf" "https://arxiv.org/pdf/2305.18323" 3
bajar "2010_malewicz_pregel.pdf" "https://kowshik.github.io/JPregel/pregel_paper.pdf" 1
bajar "1987_garcia-molina_sagas.pdf" "https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf" 1
bajar "1983_bainbridge_ironies-of-automation.pdf" "https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf" 1
bajar "2025_openai_practical-guide-to-building-agents.pdf" "https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf" 1

# --- Descarga manual (el servidor bloquea descargas automáticas) ---
echo
echo "Bajar a mano desde el navegador y guardar en $DEST/:"
echo "  2011_jegou_product-quantization.pdf  <- https://inria.hal.science/inria-00514462/document"
