python -m self_hosting_machinery.inference.inference_worker --model qwen2.5/coder/1.5b/base --compile &
PID1=$!
python -m self_hosting_machinery.inference.inference_worker --model thenlper/gte-base/cpu --compile &
PID2=$!
python -m self_hosting_machinery.scripts.enum_devices &
PID3=$!
python -m self_hosting_machinery.scripts.hf_hub_available &
PID4=$!

python -m refact_webgui.webgui.webgui --port 8009

# When webgui exits, kill background jobs
kill $PID1 $PID2 $PID3 $PID4
