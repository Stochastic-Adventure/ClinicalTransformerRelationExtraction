from transformers import (BertConfig, RobertaConfig, XLNetConfig, AlbertConfig, LongformerConfig,
                          BertTokenizer, RobertaTokenizer, XLNetTokenizer, AlbertTokenizer, LongformerTokenizer,
                          DebertaConfig, DebertaTokenizer, ElectraConfig, ElectraTokenizer, GPT2Config, GPT2Tokenizer)
from models import (BertForRelationIdentification, RoBERTaForRelationIdentification,
                    XLNetForRelationIdentification, AlbertForRelationIdentification,
                    LongFormerForRelationIdentification, DebertaForRelationIdentification,
                    ElectraForRelationIdentification, GPT2ForRelationIdentification)


EN1_START = "[s1]"
EN1_END = "[e1]"
EN2_START = "[s2]"
EN2_END = "[e2]"
# keep the seq order
SPEC_TAGS = [EN1_START, EN1_END, EN2_START, EN2_END]

MODEL_REQUIRE_SEGMENT_ID = {'bert', 'xlnet', 'albert', 'deberta'}

MODEL_DICT = {
    "bert": (BertForRelationIdentification, BertConfig, BertTokenizer),
    "roberta": (RoBERTaForRelationIdentification, RobertaConfig, RobertaTokenizer),
    "xlnet": (XLNetForRelationIdentification, XLNetConfig, XLNetTokenizer),
    "albert": (AlbertForRelationIdentification, AlbertConfig, AlbertTokenizer),
    "longformer": (LongFormerForRelationIdentification, LongformerConfig, LongformerTokenizer),
    "deberta": (DebertaForRelationIdentification, DebertaConfig, DebertaTokenizer),
    "electra": (ElectraForRelationIdentification, ElectraConfig, ElectraTokenizer),
    "gpt2": (GPT2ForRelationIdentification, GPT2Config, GPT2Tokenizer)
}

TOKENIZER_USE_FOUR_SPECIAL_TOKs = {'roberta', 'longformer', 'gpt2'}

# change VERSION if any major updates
VERSION = "0.1"
CONFIG_VERSION_NAME = "REModelVersion"

# add new args associated to version
NEW_ARGS = {"use_focal_loss": False,
            "focal_loss_gamma": 2,
            "use_binary_classification_mode": False,
            "balance_sample_weights": False}
