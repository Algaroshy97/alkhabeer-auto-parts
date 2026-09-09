from PIL import Image, ImageDraw, ImageFilter
import random

def make_sedan():
    # Create a nice sleek metallic gray background
    img = Image.new('RGB', (800, 600), (200, 205, 210))
    draw = ImageDraw.Draw(img)
    
    # Draw a generic sedan silhouette in dark gray
    # Car body
    draw.polygon([(100, 400), (150, 300), (350, 250), (550, 280), (700, 400), (700, 450), (100, 450)], fill=(80, 85, 90))
    # Windows
    draw.polygon([(200, 310), (350, 260), (450, 275), (500, 310)], fill=(180, 190, 200))
    # Wheels
    draw.ellipse((180, 410, 260, 490), fill=(20, 20, 20))
    draw.ellipse((540, 410, 620, 490), fill=(20, 20, 20))
    # Wheel rims
    draw.ellipse((200, 430, 240, 470), fill=(150, 150, 150))
    draw.ellipse((560, 430, 600, 470), fill=(150, 150, 150))
    
    # Add some smooth lighting effect (blur)
    img = img.filter(ImageFilter.GaussianBlur(1.5))
    
    img.save("assets/images/car_sedan.jpg", "JPEG", quality=90)

def make_parts():
    # Clean studio background
    img = Image.new('RGB', (800, 600), (240, 240, 245))
    draw = ImageDraw.Draw(img)
    
    # Draw generic brake pad
    draw.rounded_rectangle((100, 150, 300, 250), radius=20, fill=(70, 70, 70), outline=(50, 50, 50), width=5)
    
    # Draw generic oil filter (cylinder shape)
    draw.rectangle((400, 100, 550, 350), fill=(100, 110, 120))
    draw.ellipse((400, 70, 550, 130), fill=(80, 90, 100))
    draw.ellipse((400, 320, 550, 380), fill=(100, 110, 120))
    
    # Draw generic belt
    draw.ellipse((150, 300, 350, 500), outline=(30, 30, 30), width=20)
    
    # Draw generic spark plug
    draw.rectangle((600, 200, 640, 300), fill=(230, 230, 230))
    draw.rectangle((610, 300, 630, 400), fill=(150, 150, 160))
    draw.rectangle((615, 400, 625, 430), fill=(200, 200, 50))
    
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    img.save("assets/images/car_parts.jpg", "JPEG", quality=90)

make_sedan()
make_parts()
print("Generated images.")

def make_hero():
    # Create a dark, premium, abstract automotive silhouette
    img = Image.new('RGB', (1024, 1024), (10, 15, 25))
    draw = ImageDraw.Draw(img)
    
    # Draw a generic, smooth aerodynamic curve (like a car roof/hood line)
    # No grille, no badges, just a sleek shape
    draw.polygon([(0, 600), (300, 450), (600, 480), (1024, 650), (1024, 1024), (0, 1024)], fill=(18, 28, 45))
    draw.polygon([(0, 700), (350, 550), (700, 580), (1024, 750), (1024, 1024), (0, 1024)], fill=(25, 38, 60))
    
    # Smooth light reflections (abstract lines)
    draw.line([(100, 480), (400, 380)], fill=(40, 60, 90), width=8)
    draw.line([(400, 380), (800, 450)], fill=(40, 60, 90), width=5)
    
    # Add strong blur to make it look like a smooth, premium abstract background or macro shot
    img = img.filter(ImageFilter.GaussianBlur(15))
    
    # Add a slight dark vignette/gradient effect for contrast
    # (Achieved simply by keeping the base dark and blurred)
    
    img.save("assets/images/hero_car.jpg", "JPEG", quality=90)

make_hero()
