import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(16, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')
ax.set_facecolor('#f9f9f9')

# Координаты участников
participants = ['Client', 'System', 'Payment Gateway', 'Venue Admin', 'Contractors', 'Manager']
x_positions = [1, 3, 5, 7, 9, 11]

for i, p in enumerate(participants):
    ax.text(x_positions[i], 11, p, fontsize=12, fontweight='bold', ha='center')
    ax.plot([x_positions[i], x_positions[i]], [0, 10], color='gray', linestyle='--')

# Функция для рисования стрелок
def draw_arrow(x_start, x_end, y, text, style='->'):
    ax.annotate('', xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle='-|>', lw=2, color='black'))
    ax.text((x_start+x_end)/2, y+0.2, text, fontsize=10, ha='center', va='bottom')

# Сообщения последовательности
y = 10
draw_arrow(0, 3, y, "Check venue availability")
y -= 0.7
draw_arrow(3, 1, y, "Provide cost and conditions")
y -= 0.7
draw_arrow(1, 3, y, "Confirm booking")
y -= 0.7
draw_arrow(3, 5, y, "Request prepayment")
y -= 0.7
draw_arrow(5, 3, y, "Payment success/failure")
y -= 0.7
draw_arrow(3, 7, y, "Notify admin tasks")
y -= 0.7
draw_arrow(7, 9, y, "Assign tasks")
y -= 0.7
draw_arrow(9, 7, y, "Confirm task completion")
y -= 0.7
draw_arrow(7, 1, y, "Send event report")
y -= 0.7
draw_arrow(1, 11, y, "Collect feedback and send report")

plt.title("Event Booking Process - Sequence Diagram", fontsize=16, fontweight='bold')
plt.show()
