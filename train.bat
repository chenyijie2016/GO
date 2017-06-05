
python main.py preprocess data/test
pause
python main.py train processed_data/ --save-file=D:/savedmodel --epochs=1 --logdir=logs/my_training_run