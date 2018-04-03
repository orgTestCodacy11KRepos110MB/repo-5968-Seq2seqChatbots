from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# tensor2tensor imports
from tensor2tensor.models import transformer
from tensor2tensor.utils import registry



# Exactly replicates the base transformer model described in the paper.
@registry.register_hparams
def chatbot_cornell_base():
  hparams = transformer.transformer_base()
  hparams.learning_rate_warmup_steps=16000
  return hparams


""" Different batch sizes. """
@registry.register_hparams
def chatbot_transformer_batch_32k():
  hparams=chatbot_cornell_base()
  hparams.batch_size=32768
  return hparams

@registry.register_hparams
def chatbot_transformer_batch_16k():
  hparams=chatbot_cornell_base()
  hparams.batch_size=16384
  return hparams

@registry.register_hparams
def chatbot_transformer_batch_8k():
  hparams=chatbot_cornell_base()
  hparams.batch_size=8192
  return hparams

@registry.register_hparams
def chatbot_transformer_batch_4k():
  hparams=chatbot_cornell_base()
  hparams.batch_size=4096
  return hparams

@registry.register_hparams
def chatbot_transformer_batch_2k():
  hparams=chatbot_cornell_base()
  hparams.batch_size=2048
  return hparams


""" Different dropout values. """
@registry.register_hparams
def base_trf_20_10_drop():
  hparams = chatbot_transformer_batch_2k()
  hparams.layer_prepostprocess_dropout=0.2
  hparams.attention_dropout=0.1
  hparams.relu_dropout=0.1
  return hparams

@registry.register_hparams
def base_trf_40_20_drop():
  hparams = chatbot_transformer_batch_2k()
  hparams.layer_prepostprocess_dropout=0.4
  hparams.attention_dropout=0.2
  hparams.relu_dropout=0.2
  return hparams

@registry.register_hparams
def base_trf_50_30_drop():
  hparams = chatbot_transformer_batch_2k()
  hparams.layer_prepostprocess_dropout=0.5
  hparams.attention_dropout=0.3
  hparams.relu_dropout=0.3
  return hparams

@registry.register_hparams
def base_trf_70_50_drop():
  hparams = chatbot_transformer_batch_2k()
  hparams.layer_prepostprocess_dropout=0.7
  hparams.attention_dropout=0.5
  hparams.relu_dropout=0.5
  return hparams



""" These hparams are for my own facebook trainings. """
@registry.register_hparams
def transformer_dorka_small():
  hparams = transformer.transformer_base()
  hparams.batch_size = 8192
  hparams.max_length=256
  hparams.hidden_size=128
  hparams.num_hidden_layers=4
  hparams.filter_size=512
  hparams.num_heads=4
  hparams.learning_rate=0.02
  hparams.layer_prepostprocess_dropout=0.2
  hparams.attention_dropout=0.2
  hparams.relu_dropout=0.2

  # add a roulette wheel param
  hparams.add_hparam("roulette", "Normal")
  hparams.add_hparam("roulette_beam_size", 100)
  
  return hparams

@registry.register_hparams
def transformer_dorka_bigger():
  hparams=transformer_dorka_small()
  hparams.batch_size=4096
  hparams.hidden_size=256
  hparams.filter_size=1024
  hparams.num_heads=8
  hparams.learning_rate=0.001

  return hparams

@registry.register_hparams
def transformer_dorka_big():
  hparams=transformer.transformer_base()
  
  return hparams

@registry.register_hparams
def transformer_dorka_big_dropout():
  hparams=transformer.transformer_base()
  hparams.layer_prepostprocess_dropout=0.15
  hparams.attention_dropout=0.15
  hparams.relu_dropout=0.15

  return hparams