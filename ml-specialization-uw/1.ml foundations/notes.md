<!-- -------------------------- -->
#           Conda help            #
<!-- -------------------------- -->
conda create --name py2 python=2.7
conda create --name py3 python=3.5

conda activate py3
conda deactivate
conda remove -n py3 --all

<!-- -------------------------- -->
#        Install GraphLab         #
<!-- -------------------------- -->
conda create -n gl-env python=2.7 anaconda=4.0.0

conda activate gl-env

sudo pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/asish012@gmail.com/3662-2F8C-CC06-67B4-ED73-DFE4-9FE9-A59F/GraphLab-Create-License.tar.gz

