from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import streamlit as st

class DeploymentFunc():
    
    def subtitle_preview_generation(preview_text, size_text, color_text, font_text, vPreview):
            image_preview = ImageClip('deployment\preview\sutitle_preview1.png')
            subtitle_preview = TextClip(txt=str(preview_text), size=(float(size_text), 0), font = font_text, color = color_text)
            subtitle_preview.set_position('center')
            im_w, im_h = subtitle_preview.size
            color_clip = ColorClip(size=(int(im_w*1.1), int(im_h*1.4)),color=(0, 255, 255))
            color_clip = color_clip.set_opacity(.6)
            clip_to_overlay = CompositeVideoClip([color_clip, subtitle_preview])
            clip_to_overlay = clip_to_overlay.set_position('center')
            final_img = CompositeVideoClip([image_preview, clip_to_overlay])
            final_img.save_frame('deployment/temp/subtitle_preview.png')
            with vPreview : st.image('deployment/temp/subtitle_preview.png')