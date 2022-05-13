# Mock_project
Đây là project về lọc nhiễu tiếng ồn trong đoạn hội thoại

----
Prerequisites
---
- `Python 3.7.4` (Code được chạy với phiên bản này)
-  Cài các thư viện cằn thiết bằng `pip install -r requirements.txt`
-----

-----
Download model
-----

| Model  | Description |  Link to the model | 
| :-------------: | :---------------: | :---------------: |
| Denoising model  | Weights of the denoising model (needed for inference) | [Link](https://drive.google.com/file/d/10vaYmBLTPzsIHxL_27vD_AVJeoEHjRAd/view?usp=sharing) |---
| Lipsync student  | Weights of the student lipsync model to generate the visual stream for noisy audio inputs (needed for inference)| [Link](https://drive.google.com/file/d/1DOp9H8raua0ppywLaXYso7nALWPz_rL0/view?usp=sharing) |
| Wav2Lip teacher  |Weights of the teacher lipsync model (only needed if you want to train the network from scratch) | [Link](https://drive.google.com/file/d/1K-PF-cDD6jFyM2Lj5OvhmYdKvX5qAHZ7/view?usp=sharing)  |

---
Model denoising và wav2lip sẽ được lưu trữ tại Mock/model

Model lipsync student sẽ lưu trữ tại Mock/lipsync/model


# Data

Data được dùng là 2 tập data [LRS3](https://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrs3.html) và [VGGSound](https://www.robots.ox.ac.uk/~vgg/data/vggsound/) dataset. 

# Using
Để tiến hành dùng, chạy file deploy.py và làm theo hướng dẫn trong slide báo cáo.

# Reference
Github: https://github.com/Sindhu-Hegde/pseudo-visual-speech-denoising
Paper: https://openaccess.thecvf.com/content/WACV2021/papers/Hegde_Visual_Speech_Enhancement_Without_a_Real_Visual_Stream_WACV_2021_paper.pdf
Video demo: https://www.youtube.com/watch?v=y_oP9t7WEn4&feature=youtu.be
