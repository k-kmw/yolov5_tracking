from congestion.models import Bus


def calculate_congestion(dis, tm):
    bus = Bus.objects.last()

    cnt = bus.peopleNumber
    con = (cnt / 54) * 100

    if dis <= 24:
        if con <= 50:
            bus.congestion = "여유"
        elif con <= 90:
            bus.congestion = "보통"
        elif con <= 100:
            bus.congestion = "혼잡"
        else:
            bus.congestion = "매우 혼잡"
    else:
        if con <= 50:
            bus.congestion = "여유"
        elif con <= 85:
            bus.congestion = "보통"
        elif con <= 95:
            bus.congestion = "혼잡"
        else:
            bus.congestion = "매우 혼잡"

    bus.save()

    return {'weather': tm,
            'congestion': bus.congestion,
            'peopleNumber': bus.peopleNumber}
