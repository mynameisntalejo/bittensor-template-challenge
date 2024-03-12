<div align="center">

# **Bittensor Subnet Template** <!-- omit in toc -->

</div>
---

# Compute Requirements

1. To run a **validator**, you will need at least 24GB of VRAM. 
2. To run the default [Zephyr 7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) **miner**, you will need at least 18GB of VRAM. 

# Tools
Contexts, which are the basis of conversations, are from external APIs (which we call tools) which ensure that conversations remain grounded in factuality. Contexts are also used to obtain ground-truth answers. Currently using mathgenerator.

# Tasks
The validation process supports an ever-growing number of mathematics tasks.

Tasks contain a **query** (basic question/problem) and a **reference** (ideal answer), where a downstream HumanAgent creates a more nuanced version of the **query**.

# Running Validators
These validators are designed to run and update themselves automatically. To run a validator, follow these steps:

1. Install this repository, you can do so by following the steps outlined in [the installation section](#installation).
2. Install [Weights and Biases](https://docs.wandb.ai/quickstart) and run `wandb login` within this repository. This will initialize Weights and Biases, enabling you to view KPIs and Metrics on your validator. (Strongly recommended to help the network improve from data sharing)
3. Install [PM2](https://pm2.io/docs/runtime/guide/installation/) and the [`jq` package](https://jqlang.github.io/jq/) on your system.
   **On Linux**:
   ```bash
   sudo apt update && sudo apt install jq && sudo apt install npm && sudo npm install pm2 -g && pm2 update
   ``` 
   **On Mac OS**
   ```bash
   brew update && brew install jq && brew install npm && sudo npm install pm2 -g && pm2 update
   ```
4. Run the `run.sh` script which will handle running your validator and pulling the latest updates as they are issued. 
   ```bash
   pm2 start run.sh --name s1_validator_autoupdate -- --wallet.name <your-wallet-name> --wallet.hotkey <your-wallet-hot-key>
   ```

This will run **two** PM2 processes: one for the validator which is called `s1_validator_main_process` by default (you can change this in `run.sh`), and one for the run.sh script (in step 4, we named it `s1_validator_autoupdate`). The script will check for updates every 30 minutes, if there is an update then it will pull it, install it, restart `s1_validator_main_process` and then restart itself.

---

# Installation
This repository requires python3.8 or higher. To install, simply clone this repository and install the requirements.
```bash
git clone https://github.com/mynameisntalejo/bittensor-template-challenge.git
cd template
python -m pip install -r requirements.txt
python -m pip install -e .
```

---
# Running

Prior to running a miner or validator, you must [create a wallet](https://docs.bittensor.com/getting-started/wallets) and [register the wallet to a netuid](https://docs.bittensor.com/subnets/register-validate-mine). Once you have done so, you can run the miner and validator with the following commands.

For miners and validators running on mainnet we **strongly encourage** you to use a [local subtensor](https://github.com/opentensor/subtensor).


```bash
# To run the validator
python neurons/validator.py
    --netuid 1
    --subtensor.network <finney/local/test>
    --neuron.device cuda
    --wallet.name <your validator wallet>  # Must be created using the bittensor-cli
    --wallet.hotkey <your validator hotkey> # Must be created using the bittensor-cli
    --logging.debug # Run in debug mode, alternatively --logging.trace for trace mode

```

```bash
# To run the miner
python neurons/miners/BASE_MINER/miner.py 
    --netuid 1
    --subtensor.network <finney/local/test>
    --wallet.name <your miner wallet> # Must be created using the bittensor-cli
    --wallet.hotkey <your validator hotkey> # Must be created using the bittensor-cli
    --logging.debug # Run in debug mode, alternatively --logging.trace for trace mode
```
where `BASE_MINER` is [zephyr](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta), which is a fine-tuned Mistral-7B, however you can choose any of the supplied models found in `neurons/miners`. 
