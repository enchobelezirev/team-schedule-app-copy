import plotly.express as px


def visualize_schedule(schedule):
    df = []
    for user in schedule.employees:
        for shift in user.nextWeekShifts:
            shift_block = {
                "Employee": user.uid,
                "Start": shift.startTime,
                "Finish": shift.endTime,
            }

            df.append(shift_block)

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Employee", color="Employee")
    fig.show()
