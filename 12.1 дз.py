import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 12))
ax.set_xlim(0, 12)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_facecolor('#f0f0f0')

def draw_activity(x, y, width, height, text, color='#90EE90'):
    rect = plt.Rectangle((x, y), width, height, fill=True, edgecolor='black', facecolor=color, linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', fontsize=10, wrap=True, zorder=3)

def draw_decision(x, y, size, text):
    # Ромб для решения
    coords = [[x, y+size/2], [x+size/2, y], [x, y-size/2], [x-size/2, y]]
    polygon = plt.Polygon(coords, fill=True, edgecolor='black', facecolor='#FFD700', linewidth=2)
    ax.add_patch(polygon)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, wrap=True)

def draw_arrow(start, end, text=''):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', lw=2, color='black'))
    if text:
        mid_x = (start[0]+end[0])/2
        mid_y = (start[1]+end[1])/2
        ax.text(mid_x, mid_y + 0.2, text, fontsize=9, ha='center', va='bottom', color='black')

# Участники
participants = ['Manager', 'HR', 'Candidate', 'System', 'IT']
for i, p in enumerate(participants):
    ax.text(i*2.5+1, 13.5, p, fontsize=12, fontweight='bold', ha='center')

# Действия
draw_activity(1, 12, 2, 0.8, "Create Job Request")
draw_activity(4, 12, 2, 0.8, "Check Job Request")
draw_decision(6.5, 12.4, 0.8, "Request Valid?")
draw_activity(9, 12, 2, 0.8, "Notify Manager to Fix")
draw_activity(6.5, 11, 2, 0.8, "Approve Request")

draw_activity(1, 9, 2, 0.8, "Post Vacancy")
draw_activity(4, 9, 2, 0.8, "Receive Applications")
draw_activity(6.5, 9, 2, 0.8, "Check Applications")
draw_decision(9, 9, 0.8, "Candidate Suitable?")
draw_activity(11, 9, 2, 0.8, "Reject Application")
draw_activity(9, 7.5, 2, 0.8, "Invite to Interview")

draw_activity(1, 6, 2, 0.8, "HR Interview")
draw_activity(4, 6, 2, 0.8, "Technical Interview")
draw_decision(6.5, 6, 0.8, "Interviews Passed?")
draw_activity(9, 6, 2, 0.8, "Offer Candidate")
draw_activity(6.5, 4.5, 2, 0.8, "Reject Candidate")

draw_activity(6.5, 3, 2, 0.8, "Candidate Accepts Offer")
draw_activity(4, 1.5, 2, 0.8, "Add Employee to DB")
draw_activity(9, 1.5, 2, 0.8, "Notify IT to Setup Workspace")

# Стрелки
draw_arrow((2, 12.8), (4, 12.8))
draw_arrow((5, 12.8), (6.5, 12.8))
draw_arrow((6.5, 13.2), (6.5, 12.8), "Yes")
draw_arrow((6.5, 12.8), (9, 12.8), "No")
draw_arrow((7.5, 11.8), (6.5, 11.8))

draw_arrow((2, 9.8), (4, 9.8))
draw_arrow((5, 9.8), (6.5, 9.8))
draw_arrow((6.5, 9.4), (9, 9.4), "No")
draw_arrow((9, 8.8), (9, 7.9), "Yes")
draw_arrow((11, 9.4), (6.5, 8.9), "Return to HR")

draw_arrow((2, 6.8), (4, 6.8))
draw_arrow((5, 6.8), (6.5, 6.8))
draw_arrow((6.5, 6.4), (9, 6.4), "Yes")
draw_arrow((6.5, 5.7), (6.5, 4.9), "No")

draw_arrow((7.5, 3.8), (6.5, 3.5))
draw_arrow((5, 2.3), (4, 1.9))
draw_arrow((7.5, 2.3), (9, 1.9))

plt.title("Employee Hiring Process - Activity Diagram", fontsize=16, fontweight='bold')
plt.show()
