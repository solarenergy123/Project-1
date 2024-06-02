# Project-1
The project of GUANs' code and its dataset

Required libraries:
emd-signal-1.5.2; matplotlib-3.5.3; numpy-1.26.4; numpy-base-1.26.4; pandas-2.0.1; pyemd-1.0.0; python-3.9.12; python-dateutil-2.8.2; python-dotenv-1.0.0; scikit-learn-1.2.2; scipy-1.10.1; sympy-1.12; torch-2.0.1; torchaudio-2.0.2; torchinfo-1.8.0; torchvision-0.15.2

TTS_train.py is used to train TTS-GAN;
TTS_generate.py is used to generate fake data;
model_train.py is used to train fault diagnosis network, VGG16, and Inception V3;
model_test.py is used to get accuracy;
most models' code are saved in model.py;
GUAN.py is used to train GUAN;
GAN_LC.py is used to train TTS-GAN with LC regularization;
GAN_APA.py is used to train TTS-GAN with APA;
G_EVALUATE.py is used to evaluate fake data;
draw_picture.py is used to draw pictures in paper;

All experimental data are saved in "data" file;
All simulation data are saved in "data_mat" file;
The "sim" file is used to train and test siamese network.
