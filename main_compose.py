import hydra
from omegaconf import DictConfig, OmegaConf

def main():
    # global initialization
    hydra.initialize(config_path="./cfg", job_name="global_compose")
    cfg = hydra.compose(config_name="config", overrides=["communication=uart"])
    
    print("Hello Hydra!")
    print(OmegaConf.to_yaml(cfg))
    

if __name__=="__main__":
    main()