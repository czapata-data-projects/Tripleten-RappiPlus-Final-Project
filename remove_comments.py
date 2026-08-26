import json

# Load the notebook
with open('S12 Estudiante_Proyecto_Final.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Filter out cells that contain reviewer comments
filtered_cells = []
for cell in notebook['cells']:
    # Skip markdown cells that contain reviewer comments
    if cell['cell_type'] == 'markdown':
        source_text = ''.join(cell['source'])
        if 'Comentario del revisor' in source_text or 'Review General' in source_text or 'Respuesta de estudiante' in source_text:
            print(f"Removing comment cell: {cell['id']}")
            continue
    filtered_cells.append(cell)

# Update notebook with filtered cells
notebook['cells'] = filtered_cells

# Save the modified notebook
with open('S12 Estudiante_Proyecto_Final.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("✓ Reviewer comments removed successfully!")
print(f"✓ Notebook now has {len(filtered_cells)} cells (removed 2 comment cells)")
