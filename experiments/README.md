# Исследования

Скрипты, которыми получены цифры раздела «Что пробовали и почему отказались» в `REPORT.md`.
В сервис они не входят. Запуск — из корня проекта, сначала один раз создать кэш набора:

```bash
python experiments/make_cache.py --data /path/to/НД_для_обучения   # → out/cache.pkl
```

| Скрипт | Что проверяет |
|---|---|
| `eval_axis.py` | ось позвоночника против разметки врачей, картинки линий |
| `eval_roi.py` | отступы области интереса бедра против разметки |
| `eval_rotation.py` | признаки ротации бедра (малый вертел, офсет), в т. ч. по маскам SAM |
| `embed.py` | признаки SigLIP / CLIP (нужны `torch`, `transformers`) |
| `eval_rot_models.py` | SigLIP и CLIP для ротации бедра, варианты кропов |
| `perm_test.py` | перестановочный тест для SigLIP (контроль утечек) |
| `sam_prompts.py`, `sam_run.py`, `sam_view.py` | маски бедра SAM / MedSAM |
| `vlm_probe.py` | локальная VLM Qwen3-VL-2B на посторонних предметах |
| `colab/` | дообучение SigLIP в Google Colab |
| `make_slides.py` | иллюстрации по оси позвоночника |

Часть скриптов читает результаты предыдущих: `embed.py` → `eval_rot_models.py`, `perm_test.py`, `vlm_probe.py`;
`eval_rotation.py` → `eval_rot_models.py`; `sam_prompts.py` → `sam_run.py` → `sam_view.py`.

Итог: ни один нейросетевой вариант не улучшил измерения по ТЗ на этом наборе (6–36 нарушений
на критерий); SigLIP как третья оценка ротации ухудшал F1 0.70 → 0.63 и был убран.
