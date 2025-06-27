from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel


#Base model on your local filesystem
base_model_dir = "/home/syu2/.refact/perm-storage/weights/models--codellama--CodeLlama-7b-hf/snapshots/6c284d1468fe6c413cf56183e69b194dcfa27fe6/"
base_model = AutoModelForCausalLM.from_pretrained(base_model_dir)
tokenizer = AutoTokenizer.from_pretrained(base_model_dir)

#Adaptor directory on your local filesystem
adaptor_dir = "/home/syu2/.refact/perm-storage/loras/tbkcode_experiment_01/checkpoints/iter1050-testloss0.676/"
merged_model = PeftModel.from_pretrained(base_model,adaptor_dir)

merged_model = merged_model.merge_and_unload()
merged_model.save_pretrained("/home/syu2/.refact/perm-storage/loras/tbkcode_experiment_01/merged_model_iteration1005")
tokenizer.save_pretrained("/home/syu2/.refact/perm-storage/loras/tbkcode_experiment_01/merged_model_iteration1005", legacy_format=False)