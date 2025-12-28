# CorkBoard-Planner  

An in-works pygame app that's essentially a corkboard planner.  

## Why do this?   

Couple reasons:  
- This is for me to plan out my future projects like the complex module systems of my `pygame_template V2`  
- This visualised planning style seems to resonate with me  
- This directly implements some of the features I want to add to the GUI module of `pygame_template V2`  

(Part of the reason this exists is to be a good code example of my [`pygame_template V1`](https://github.com/FINN-2005/pygame_template))  

## What's the plan?  

If you’ve seen any normal amount of mystery/crime/investigation movies, you already know what a corkboard planner looks like.  
I’m basically making that.  

### Core Features  

- Infinitely tileable corkboard with panning and zooming  
- Element Drawer at the bottom (papers, strings, pins, etc.)  
- Top Drawer for **File / Settings / Help** style stuff  
- Floating side window for creating and editing elements  

### Papers  

- 3 types planned:
  - Text  
  - Image  
  - Drawable canvas  
- Random colours  
- Slight random rotation  
- Can be duplicated or saved as templates  

### Interactions / UX  

- Drag papers around the board  
- Bring paper to front on select (Z-ordering / layering)  
- Resize papers  
- Optional snapping behaviour  
- Camera pan + zoom (already implemented)  

### Right-Click Menu (planned)

Stuff like:  

- copy / paste  
- cut / delete  
- duplicate  
- undo / redo  
- bring to front / send to back  

### Linking & Decoration  

- Pins  
- Strings between papers  
- Slight jitter / realism vibes  
- Drop shadows for depth  

### Under-the-hood Stuff I’m Playing With  

- grid-based hit detection (spatial hash / skip-list-ish)  
- zoom-aware rendering  
- caching rotated/scaled paper surfaces  
- chunked tile renderer for the cork texture  

### Saving & Exporting  

- save/load projects (JSON-like format)  
- import existing plans  
- maybe export screenshots later  

### Distribution  

- this will eventually be packaged as an `.exe`  
- and released here when it’s decent enough  

---
## What I Have Right Now  

- An infinitely tilebale corkboard  
- spand and zoom capabilities  
- And start of the Paper class  
- Plans for page content system and major future code factoring with performance optimisation  
