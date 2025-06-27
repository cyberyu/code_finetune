from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

#Base model on your local filesystem
base_model_dir = "/home/syu2/.refact/perm-storage/weights/models--codellama--CodeLlama-7b-hf/snapshots/6c284d1468fe6c413cf56183e69b194dcfa27fe6/"
#base_model_dir = "/home/syu2/.cache/huggingface/hub/models--meta-llama--Llama-3.1-8B-Instruct/snapshots/0e9e39f249a16976918f6564b8830bc894c89659/"
base_model = AutoModelForCausalLM.from_pretrained(base_model_dir)
tokenizer = AutoTokenizer.from_pretrained(base_model_dir)

#Adaptor directory on your local filesystem
adaptor_dir = "/home/syu2/.refact/perm-storage/loras/tbkcode_experiment_01/checkpoints/iter0010-testloss1.152/"
merged_model = PeftModel.from_pretrained(base_model,adaptor_dir)

merged_model = merged_model.merge_and_unload()
merged_model.save_pretrained("/home/syu2/.refact/perm-storage/loras/tbkcode_experiment_01/merged_model_iteration0010")
tokenizer.save_pretrained("/home/syu2/.refact/perm-storage/loras/tbkcode_experiment_01/merged_model_iteration0010", legacy_format=False)
