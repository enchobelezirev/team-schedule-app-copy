import plotly.express as px


def visualize_schedule(schedule):
    df = []
    for user in schedule.employees:
        for shift in user.next_week_shifts:
            shift_block = {
                "Employee": user.uid,
                "Start": shift.start_time,
                "Finish": shift.end_time,
            }

            df.append(shift_block)

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Employee", color="Employee")
    fig.show()
