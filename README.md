# Mock_project
Đây là project về lọc nhiễu tiếng ồn trong đoạn hội thoại
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
----
Model lipsync student sẽ lưu trữ tại Mock/lipsync/model
----
