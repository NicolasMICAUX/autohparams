<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]<!--[![Forks][forks-shield]][forks-url]-->
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]<!--[![MIT License][license-shield]][license-url]--><!--[![LinkedIn][linkedin-shield]][linkedin-url]-->
[![PyPi version][pypi-shield]][pypi-url]
[![Python 2][python2-shield]][python-url]
[![Python 3][python3-shield]][python-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <a href="https://github.com/NicolasMICAUX/autohparams">
    <img src="https://raw.githubusercontent.com/NicolasMICAUX/autohparams/main/images/logo.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">AutoHparams</h3>

  <p align="center">
    Créez automatiquement une configuration d'hyper-paramètres à partir de variables globales!
    <br />
<!--
    <a href="https://github.com/NicolasMICAUX/autohparams"><strong>Explorer la doc »</strong></a>
-->
    <br />
    ·
    <a href="https://github.com/NicolasMICAUX/autohparams/issues">Signaler un bug</a>
</div>


<!-- ABOUT THE PROJECT -->
## À propos

<!-- [Screen Shot][product-screenshot] -->

Avez-vous déjà effectué une expérience de machine learning pendant des heures, juste pour vous rendre compte quelques jours plus tard que vous avez oublié de sauvegarder certains hyper-paramètres? Alors vous devez prier pour que votre mémoire soit bonne, ou tout recommencer?

AutoHparams est un outil qui sauvegarde chaque variable de la portée globale de votre code dans un dictionnaire, que vous pouvez ensuite enregistrer à l'aide de votre outil préféré. Cela permet d'éviter 80% des situations d'hyper-paramètres oubliés.

<!-- GETTING STARTED -->
## Getting Started
AutoHparams s'utilise en une ligne.

Installez AutoHparams avec pip :
```sh
pip install autohparams
```

Importez-le dans votre code, en ajoutant cette ligne :
```python
from autohparams import get_auto_hparams
```

Pour obtenir le dictionnaire de hparamsuration, faites simplement :
```python
hparams = get_auto_hparams(globals())
```

**Advanced tip**  
Par défaut, `get_auto_hparams` ignore les variables dont le nom commence par un trait de soulignement` _`. Pratique pour filtrer les variables que vous souhaitez inclure dans la hparamsuration.
Par exemple:
```python	
lr = 0.001  # nous voulons inclure le taux d'apprentissage
bs = 64     # nous voulons inclure la taille de lot
_gpu = 0    # nous ne voulons pas inclure le GPU choisi
hparams = get_auto_hparams(globals())
```

<!-- USAGE EXAMPLES -->
## Usage
Vous pouvez maintenant l'utiliser dans n'importe quel cadre de votre choix, par exemple :

**Tensorboard**
```python
import tensorflow as tf
from tensorboard.plugins.hparams import api as hp

with tf.summary.create_file_writer('logs/hparam_tuning').as_default():
  hp.hparams(hparams)
```

**MLflow**
```python
import mlflow

with mlflow.start_run():
  mlflow.log_params(hparams)
```

**Weights & Biases (wandb)**
```python
import wandb

wandb.init(hparams=hparams)
```

**Comet.ml**
```python
from comet_ml import Experiment

experiment = Experiment()
experiment.log_parameters(hparams)
```

**Neptune.ai**
```python
import neptune.new as neptune

run = neptune.init()

run['parameters'] = hparams
```

**Pytorch Lightning**
```python
import pytorch_lightning as pl

trainer = pl.Trainer(logger=...)
trainer.logger.log_hyperparams(hparams)
```

**Guild AI**
```python
import guild

guild.run(hparams=hparams)
```

**Polyaxon**
```python
import polyaxon_sdk

api_client = polyaxon_sdk.ApiClient()
api_client.create_hyper_params(run_uuid='uuid-of-your-run', body=hparams)
```

**ClearML**
```python
from clearml import Task

task = Task.init()
task.set_parameters(hparams)
```

**Kubeflow**
```python
from kubeflow.metadata import metadata

store = metadata.Store()
store.log_metadata(hparams)
```

#### Encore plus concis
Si vous êtes amateur de la sorcellerie de python, vous pouvez même import autohparams et l'utiliser comme une fonction:
```python
import autohparams
config = autohparams(globals())
```
On ne peut pas faire plus simple !

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing 
Contributions are welcome!  

<!-- ROADMAP-->
### Roadmap/todo
<!-- table with columns : task, importance, difficulty, status, description -->
<!-- 
| Task                     | Importance | Difficulty | Contributor on it | Description                                                                                                                                    |
|:-------------------------|------------|------------|-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [Write some tests](https://github.com/NicolasMICAUX/autohparams/discussions/5)         | 4/5        | 2/5        | NOBODY            | Write some tests to ensure that the code is working properly.                                                                                  |
| [Profile code](https://github.com/NicolasMICAUX/autohparams/discussions/11)             | 2/5        | 1/5        | NOBODY            | Profile the code to see if we can speed it up a little.                                                                                        |
-->

Non-Code contribution :

| Task                     | Importance | Difficulty | Contributor on it | Description                                                                                                                                                           |
|:-------------------------|------------|------------|-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Adding documentation](https://github.com/NicolasMICAUX/autohparams/discussions/6)     | 4/5        | 1/5        | NOBODY            | Write basic tutorials with real-life scenarios, write a wiki for other contributors to better understand the functioning of the library. |


_For every todo, just click on the link to find the discussion where I describe how I would do it._  
See the [discussions](https://github.com/NicolasMICAUX/autohparams/discussions) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### How to contribute
Contributing is an awesome way to learn, inspire, and help others. Any contributions you make are **greatly appreciated**, even if it's just about styling and best practices.

If you have a suggestion that would make this project better, please fork the repo and create a pull request.  
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Authors
This library was created by [Nicolas MICAUX](https://github.com/NicolasMICAUX).


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NicolasMICAUX/autohparams.svg?style=for-the-badge
[contributors-url]: https://github.com/NicolasMICAUX/autohparams/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/NicolasMICAUX/autohparams.svg?style=for-the-badge
[stars-url]: https://github.com/NicolasMICAUX/autohparams/stargazers
[issues-shield]: https://img.shields.io/github/issues/NicolasMICAUX/autohparams.svg?style=for-the-badge
[issues-url]: https://github.com/NicolasMICAUX/autohparams/issues
[pypi-shield]: https://img.shields.io/pypi/v/searchin.svg?style=for-the-badge
[pypi-url]: https://pypi.org/project/searchin/
[python2-shield]: https://img.shields.io/badge/python-2.7+-blue.svg?style=for-the-badge
[python3-shield]: https://img.shields.io/badge/python-3.5+-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/downloads/

[//]: # ([license-shield]: https://img.shields.io/github/license/NicolasMICAUX/autohparams.svg?style=for-the-badge)
[//]: # ([license-url]: https://github.com/NicolasMICAUX/autohparams/blob/master/LICENSE.txt)
[//]: # ([linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)
[//]: # ([linkedin-url]: https://linkedin.com/in/othneildrew)
