import hydra
from omegaconf import DictConfig, OmegaConf

##################################################
# Override Config
# $ python main.py communication=uart
##################################################

@hydra.main(config_path="./cfg", config_name="config")
def main(cfg: DictConfig):
    print("Hello Hydra!")
    print(OmegaConf.to_yaml(cfg))
    

if __name__=="__main__":
    main()