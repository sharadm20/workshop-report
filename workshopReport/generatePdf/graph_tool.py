from django.conf import settings
import os
import matplotlib.pyplot as plt


def pie_chart_save_image(sizes, labels, filename):
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(os.path.join(settings.BASE_DIR, filename))


def bar_chart_save_image(objects, performance, filename, y_label, q):
    fig2, ax2 = plt.subplots()
    ax2.set_xbound(lower=0, upper=10)
    plt.bar(objects, performance, align='center')
    plt.xticks(objects)
    plt.ylabel(y_label)
    title = dict([(7, 'Introduction'),
                  (8, 'IO'),
                  (9, 'Motor'),
                  (10, 'PWM'),
                  (11, 'LCD'),
                  (12, 'ADC'),
                  (13, 'White Line Follower'),
                  (14, 'Interrupt')])
    plt.title(title[q])
    plt.savefig(os.path.join(settings.BASE_DIR, filename))
