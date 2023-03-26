def frames_per_second(frame, minutes):
    f_p_s = frame * 60 * minutes
    return f_p_s


print(frames_per_second(1, 1))
print(frames_per_second(10, 1))
print(frames_per_second(10, 25))
