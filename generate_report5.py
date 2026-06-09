#!/usr/bin/env python3
"""Generate report_data5.html for DE01 C04-011, 20.05.2026 – 09.06.2026."""

from datetime import date
from collections import defaultdict
import json, re

# ── Raw data ─────────────────────────────────────────────────────────────────
# Columns: SHIFT, HOUR, PROD_TARGET, PRODUCED, REPORTED, GOOD, GOOD_FIRST,
#          GOOD_FIRST_RATIO, NCR, ACTIVE_NCR, REWORK, SCRAP, RAW_SCRAP,
#          REINTRO_REWORKED, REINTRO_PARTIAL, REINTRODUCED
RAW = [
    ('S3 22. May 26', '3 S3 22. May 26', 189, 219, 204, 203, 203, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S2 8. Jun 26', '15 S2 8. Jun 26', 189, 219, 168, 168, 168, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 25. May 26', '23 S3 25. May 26', 189, 216, 219, 219, 219, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 26. May 26', '9 S1 26. May 26', 189, 216, 186, 186, 186, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 26. May 26', '12 S1 26. May 26', 189, 216, 195, 195, 167, 0.856410256410256, 0, 0, 0, 0, 0, 0, 28, 28),
    ('S3 22. May 26', '23 S3 22. May 26', 189, 210, 189, 189, 189, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 26. May 26', '19 S2 26. May 26', 189, 210, 210, 210, 210, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 26. May 26', '17 S2 26. May 26', 189, 201, 207, 204, 204, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S1 20. May 26', '11 S1 20. May 26', 172, 200, 114, 114, 114, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 20. May 26', '12 S1 20. May 26', 172, 200, 144, 134, 134, 1, 10, 0, 0, 10, 0, 0, 0, 0),
    ('S3 21. May 26', '1 S3 21. May 26', 168, 196, 74, 74, 74, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 31. May 26', '23 S3 31. May 26', 0, 186, 192, 186, 186, 1, 6, 0, 0, 6, 0, 0, 0, 0),
    ('S1 20. May 26', '6 S1 20. May 26', 172, 184, 112, 101, 101, 1, 11, 0, 0, 11, 0, 0, 0, 0),
    ('S2 26. May 26', '15 S2 26. May 26', 189, 183, 144, 126, 126, 1, 18, 0, 0, 18, 0, 0, 0, 0),
    ('S1 20. May 26', '7 S1 20. May 26', 172, 180, 108, 108, 108, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 8. Jun 26', '9 S1 8. Jun 26', 189, 180, 180, 180, 180, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 8. Jun 26', '17 S2 8. Jun 26', 189, 180, 159, 159, 159, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 8. Jun 26', '1 S3 8. Jun 26', 189, 177, 180, 180, 180, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 26. May 26', '8 S1 26. May 26', 189, 174, 186, 186, 186, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 31. May 26', '3 S3 31. May 26', 0, 174, 174, 171, 171, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S2 8. Jun 26', '14 S2 8. Jun 26', 189, 174, 153, 153, 150, 0.980392156862745, 0, 0, 0, 0, 0, 0, 0, 3),
    ('S3 8. Jun 26', '23 S3 8. Jun 26', 189, 174, 180, 176, 176, 1, 4, 0, 0, 4, 0, 0, 0, 0),
    ('S3 21. May 26', '3 S3 21. May 26', 168, 172, 118, 105, 105, 1, 13, 0, 0, 13, 0, 0, 0, 0),
    ('S2 26. May 26', '14 S2 26. May 26', 189, 171, 165, 155, 155, 1, 10, 0, 0, 10, 0, 0, 0, 0),
    ('S3 22. May 26', '22 S3 22. May 26', 189, 168, 168, 168, 165, 0.982142857142857, 0, 0, 0, 0, 0, 0, 3, 3),
    ('S1 26. May 26', '6 S1 26. May 26', 189, 165, 156, 156, 153, 0.980769230769231, 0, 0, 0, 0, 0, 0, 0, 3),
    ('S1 26. May 26', '11 S1 26. May 26', 189, 165, 165, 165, 165, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 25. May 26', '22 S3 25. May 26', 189, 162, 159, 156, 153, 0.980769230769231, 3, 0, 0, 3, 0, 0, 3, 3),
    ('S2 26. May 26', '21 S2 26. May 26', 189, 162, 164, 161, 42, 0.260869565217391, 3, 0, 0, 3, 0, 0, 117, 119),
    ('S1 8. Jun 26', '11 S1 8. Jun 26', 189, 162, 171, 168, 168, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S2 8. Jun 26', '19 S2 8. Jun 26', 189, 162, 132, 132, 132, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 21. May 26', '22 S3 21. May 26', 168, 161, 105, 73, 70, 0.958904109589041, 31, 1, 0, 31, 0, 0, 3, 3),
    ('S1 3. Jun 26', '7 S1 3. Jun 26', 168, 156, 178, 175, 175, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S3 8. Jun 26', '22 S3 8. Jun 26', 189, 153, 147, 140, 140, 1, 4, 0, 0, 4, 0, 0, 0, 0),
    ('S3 22. May 26', '0 S3 22. May 26', 189, 147, 165, 165, 165, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 22. May 26', '1 S3 22. May 26', 189, 147, 135, 132, 132, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S3 8. Jun 26', '3 S3 8. Jun 26', 189, 147, 150, 137, 137, 1, 13, 0, 0, 13, 0, 0, 0, 0),
    ('S3 25. May 26', '5 S3 25. May 26', 189, 144, 147, 124, 36, 0.290322580645161, 23, 0, 0, 23, 0, 0, 88, 88),
    ('S1 3. Jun 26', '9 S1 3. Jun 26', 168, 144, 125, 125, 125, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 8. Jun 26', '0 S3 8. Jun 26', 189, 144, 138, 138, 138, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 25. May 26', '4 S3 25. May 26', 189, 141, 147, 134, 134, 1, 13, 0, 0, 13, 0, 0, 0, 0),
    ('S3 22. May 26', '4 S3 22. May 26', 189, 138, 153, 153, 80, 0.522875816993464, 0, 0, 0, 0, 0, 0, 73, 73),
    ('S3 25. May 26', '1 S3 25. May 26', 189, 138, 138, 136, 136, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S3 25. May 26', '3 S3 25. May 26', 189, 138, 129, 104, 104, 1, 25, 0, 0, 25, 0, 0, 0, 0),
    ('S3 31. May 26', '0 S3 31. May 26', 0, 138, 135, 130, 130, 1, 5, 0, 0, 5, 0, 0, 0, 0),
    ('S1 8. Jun 26', '12 S1 8. Jun 26', 189, 135, 135, 131, 131, 1, 4, 0, 0, 4, 0, 0, 0, 0),
    ('S2 8. Jun 26', '16 S2 8. Jun 26', 189, 135, 156, 156, 156, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 8. Jun 26', '4 S3 8. Jun 26', 189, 135, 123, 122, 122, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S1 29. May 26', '12 S1 29. May 26', 168, 132, 134, 126, 126, 1, 8, 0, 0, 8, 0, 0, 0, 0),
    ('S3 31. May 26', '4 S3 31. May 26', 0, 132, 129, 107, 81, 0.757009345794392, 22, 0, 0, 22, 0, 0, 26, 26),
    ('S1 26. May 26', '7 S1 26. May 26', 189, 126, 123, 117, 117, 1, 6, 0, 0, 6, 0, 0, 0, 0),
    ('S1 20. May 26', '9 S1 20. May 26', 172, 124, 90, 66, 66, 1, 24, 0, 0, 24, 0, 0, 0, 0),
    ('S3 22. May 26', '5 S3 22. May 26', 189, 123, 126, 126, None, None, 0, 0, 0, 0, 0, 0, 126, 126),
    ('S2 26. May 26', '20 S2 26. May 26', 189, 123, 124, 114, 113, 0.991228070175439, 10, 0, 0, 10, 0, 0, 0, 1),
    ('S2 26. May 26', '16 S2 26. May 26', 189, 120, 156, 138, 138, 1, 18, 0, 0, 18, 0, 0, 0, 0),
    ('S1 29. May 26', '9 S1 29. May 26', 168, 120, 131, 131, 131, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 31. May 26', '22 S3 31. May 26', 0, 120, 114, 108, 105, 0.972222222222222, 6, 0, 0, 6, 0, 0, 3, 3),
    ('S1 3. Jun 26', '11 S1 3. Jun 26', 168, 120, 138, 138, 138, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 21. May 26', '23 S3 21. May 26', 168, 116, 157, 105, 105, 1, 52, 0, 0, 52, 0, 0, 0, 0),
    ('S1 26. May 26', '10 S1 26. May 26', 189, 111, 132, 132, 132, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 25. May 26', '0 S3 25. May 26', 189, 108, 108, 108, 108, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 25. May 26', '2 S3 25. May 26', 189, 108, 108, 108, 108, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 8. Jun 26', '13 S1 8. Jun 26', 189, 108, 108, 96, 0, 0, 12, 0, 0, 12, 0, 0, 96, 96),
    ('S1 29. May 26', '7 S1 29. May 26', 168, 105, 62, 58, 58, 1, 4, 0, 0, 4, 0, 0, 0, 0),
    ('S3 31. May 26', '1 S3 31. May 26', 0, 105, 105, 47, 47, 1, 58, 0, 0, 58, 0, 0, 0, 0),
    ('S1 8. Jun 26', '8 S1 8. Jun 26', 189, 105, 102, 101, 101, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S3 21. May 26', '0 S3 21. May 26', 168, 104, 106, 100, 100, 1, 6, 0, 0, 6, 0, 0, 0, 0),
    ('S1 29. May 26', '8 S1 29. May 26', 168, 104, 70, 70, 70, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 29. May 26', '13 S1 29. May 26', 168, 104, 168, 141, 141, 1, 27, 0, 0, 27, 0, 0, 0, 0),
    ('S3 31. May 26', '5 S3 31. May 26', 0, 102, 105, 93, 0, 0, 12, 0, 0, 12, 0, 0, 93, 93),
    ('S1 3. Jun 26', '12 S1 3. Jun 26', 168, 100, 72, 72, 72, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 26. May 26', '18 S2 26. May 26', 189, 99, 99, 97, 97, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S1 3. Jun 26', '8 S1 3. Jun 26', 168, 96, 105, 105, 105, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 3. Jun 26', '10 S1 3. Jun 26', 168, 92, 50, 50, 50, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 29. May 26', '11 S1 29. May 26', 168, 91, 104, 104, 104, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 8. Jun 26', '6 S1 8. Jun 26', 189, 90, 69, 60, 57, 0.95, 9, 0, 0, 9, 0, 0, 3, 3),
    ('S1 8. Jun 26', '7 S1 8. Jun 26', 189, 87, 108, 87, 87, 1, 21, 0, 0, 21, 0, 0, 0, 0),
    ('S1 29. May 26', '6 S1 29. May 26', 168, 84, 42, 42, 38, 0.904761904761905, 0, 0, 0, 0, 0, 0, 0, 4),
    ('S1 29. May 26', '10 S1 29. May 26', 168, 84, 49, 49, 49, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 8. Jun 26', '20 S2 8. Jun 26', 189, 84, 114, 114, 114, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 8. Jun 26', '21 S2 8. Jun 26', 189, 84, 138, 129, 129, 1, 9, 0, 0, 9, 0, 0, 0, 0),
    ('S1 20. May 26', '13 S1 20. May 26', 172, 80, 253, 224, 220, 0.982142857142857, 29, 0, 0, 29, 0, 0, 0, 4),
    ('S1 21. May 26', '7 S1 21. May 26', 63, 77, 73, 73, 73, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 20. May 26', '8 S1 20. May 26', 172, 76, 91, 91, 91, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 21. May 26', '9 S1 21. May 26', 63, 76, 77, 77, 76, 0.987012987012987, 0, 0, 0, 0, 0, 0, 0, 1),
    ('S2 5. Jun 26', '17 S2 5. Jun 26', 63, 76, 74, 74, 74, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 21. May 26', '6 S1 21. May 26', 63, 74, 69, 69, 69, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 20. May 26', '3 S3 20. May 26', 63, 73, 73, 71, 71, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S2 8. Jun 26', '18 S2 8. Jun 26', 189, 72, 90, 90, 90, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 2. Jun 26', '19 S2 2. Jun 26', 63, 71, 70, 70, 70, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 20. May 26', '23 S3 20. May 26', 63, 70, 71, 71, 71, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 20. May 26', '1 S3 20. May 26', 63, 70, 70, 68, 68, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S1 21. May 26', '11 S1 21. May 26', 63, 70, 70, 68, 68, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S3 20. May 26', '22 S3 20. May 26', 63, 69, 68, 68, 67, 0.985294117647059, 0, 0, 0, 0, 0, 0, 0, 1),
    ('S3 8. Jun 26', '2 S3 8. Jun 26', 189, 69, 69, 68, 68, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S3 21. May 26', '4 S3 21. May 26', 168, 68, 47, 35, 35, 1, 12, 0, 0, 12, 0, 0, 0, 0),
    ('S2 2. Jun 26', '14 S2 2. Jun 26', 63, 68, 65, 60, 60, 1, 5, 0, 0, 5, 0, 0, 0, 0),
    ('S2 2. Jun 26', '16 S2 2. Jun 26', 63, 67, 66, 66, 66, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 5. Jun 26', '14 S2 5. Jun 26', 57.75, 66, 64, 48, 47, 0.979166666666667, 16, 0, 0, 16, 0, 0, 0, 1),
    ('S2 5. Jun 26', '21 S2 5. Jun 26', 63, 66, 67, 67, 67, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 8. Jun 26', '10 S1 8. Jun 26', 189, 66, 60, 54, 54, 1, 6, 0, 0, 6, 0, 0, 0, 0),
    ('S1 21. May 26', '8 S1 21. May 26', 63, 65, 72, 70, 70, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S3 22. May 26', '2 S3 22. May 26', 189, 63, 75, 75, 75, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 31. May 26', '2 S3 31. May 26', 0, 63, 66, 63, 63, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S2 2. Jun 26', '17 S2 2. Jun 26', 63, 63, 65, 65, 65, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 5. Jun 26', '23 S3 5. Jun 26', 63, 63, 64, 64, 64, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 5. Jun 26', '0 S3 5. Jun 26', 63, 61, 60, 60, 60, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 26. May 26', '13 S1 26. May 26', 189, 60, 90, 84, 0, 0, 6, 0, 0, 6, 0, 0, 84, 84),
    ('S1 21. May 26', '12 S1 21. May 26', 63, 59, 46, 45, 45, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S1 27. May 26', '11 S1 27. May 26', 63, 57, 58, 58, 58, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 2. Jun 26', '21 S2 2. Jun 26', 63, 57, 58, 54, 54, 1, 4, 0, 0, 4, 0, 0, 0, 0),
    ('S3 5. Jun 26', '22 S3 5. Jun 26', 56.7, 57, 56, 56, 55, 0.982142857142857, 0, 0, 0, 0, 0, 0, 0, 1),
    ('S3 5. Jun 26', '1 S3 5. Jun 26', 63, 57, 56, 53, 53, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S3 5. Jun 26', '4 S3 5. Jun 26', 63, 56, 52, 52, 52, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 21. May 26', '13 S1 21. May 26', 63, 54, 69, 69, 69, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 5. Jun 26', '20 S2 5. Jun 26', 63, 54, 55, 55, 55, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S2 5. Jun 26', '19 S2 5. Jun 26', 63, 53, 51, 40, 40, 1, 11, 0, 0, 11, 0, 0, 0, 0),
    ('S2 2. Jun 26', '15 S2 2. Jun 26', 63, 52, 54, 49, 49, 1, 5, 0, 0, 5, 0, 0, 0, 0),
    ('S3 5. Jun 26', '3 S3 5. Jun 26', 63, 50, 55, 53, 53, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S3 21. May 26', '5 S3 21. May 26', 168, 48, 190, 187, 175, 0.935828877005348, 4, 0, 0, 3, 0, 0, 12, 12),
    ('S1 27. May 26', '6 S1 27. May 26', 63, 47, 42, 36, 36, 1, 6, 0, 0, 6, 0, 0, 0, 0),
    ('S1 27. May 26', '7 S1 27. May 26', 63, 46, 34, 29, 29, 1, 5, 0, 0, 5, 0, 0, 0, 0),
    ('S2 5. Jun 26', '15 S2 5. Jun 26', 63, 46, 47, 43, 43, 1, 4, 0, 0, 4, 0, 0, 0, 0),
    ('S1 27. May 26', '13 S1 27. May 26', 63, 45, 55, 46, 45, 0.978260869565217, 9, 0, 0, 9, 0, 0, 0, 1),
    ('S2 5. Jun 26', '16 S2 5. Jun 26', 63, 45, 45, 40, 40, 1, 5, 0, 0, 5, 0, 0, 0, 0),
    ('S1 3. Jun 26', '6 S1 3. Jun 26', 168, 44, None, None, None, None, None, None, None, None, None, None, None, None),
    ('S1 3. Jun 26', '13 S1 3. Jun 26', 168, 44, 128, 125, 121, 0.968, 3, 0, 0, 3, 0, 0, 0, 4),
    ('S2 2. Jun 26', '20 S2 2. Jun 26', 63, 42, 44, 42, 41, 0.976190476190476, 2, 0, 0, 2, 0, 0, 0, 1),
    ('S1 21. May 26', '10 S1 21. May 26', 63, 41, 40, 39, 39, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S1 27. May 26', '12 S1 27. May 26', 63, 41, 36, 36, 36, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 20. May 26', '4 S3 20. May 26', 63, 40, 37, 34, 34, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S3 20. May 26', '0 S3 20. May 26', 63, 35, 35, 33, 33, 1, 2, 0, 0, 2, 0, 0, 0, 0),
    ('S3 5. Jun 26', '5 S3 5. Jun 26', 63, 35, 40, 40, 40, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 27. May 26', '8 S1 27. May 26', 63, 34, 46, 39, 39, 1, 7, 0, 0, 7, 0, 0, 0, 0),
    ('S1 27. May 26', '10 S1 27. May 26', 63, 33, 28, 28, 28, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 27. May 26', '9 S1 27. May 26', 63, 32, 20, 20, 20, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 20. May 26', '2 S3 20. May 26', 63, 31, 31, 30, 30, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S2 5. Jun 26', '18 S2 5. Jun 26', 63, 31, 34, 34, 34, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S3 8. Jun 26', '5 S3 8. Jun 26', 189, 27, None, None, None, None, None, None, None, None, None, None, None, None),
    ('S3 20. May 26', '5 S3 20. May 26', 63, 26, 29, 26, 26, 1, 3, 0, 0, 3, 0, 0, 0, 0),
    ('S2 2. Jun 26', '18 S2 2. Jun 26', 63, 20, 19, 10, 10, 1, 9, 0, 0, 9, 0, 0, 0, 0),
    ('S3 5. Jun 26', '2 S3 5. Jun 26', 63, 19, 15, 14, 14, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ('S1 20. May 26', '10 S1 20. May 26', 172, 11, 47, 47, 47, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ('S1 2. Jun 26', '13 S1 2. Jun 26', 63, 1, None, None, None, None, None, None, None, None, None, None, None, None),
    ('S3 21. May 26', '2 S3 21. May 26', None, None, 71, 71, 71, 1, 0, 0, 0, 0, 0, 0, 0, 0),
]

# ── Helper: extract hour number from HOUR string ──────────────────────────────
def extract_hour(h_str):
    m = re.match(r'^(\d+)\s', h_str)
    return int(m.group(1)) if m else None

# ── Helper: extract date key from SHIFT string, return sortable tuple ─────────
MONTH_MAP = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
}

def shift_sort_key(shift_str):
    """Return (year, month, day) tuple for sorting."""
    m = re.search(r'(\d+)\.\s+(\w+)\s+(\d+)', shift_str)
    if not m:
        return (9999, 99, 99)
    day = int(m.group(1))
    mon = MONTH_MAP.get(m.group(2), 99)
    yr = int(m.group(3))
    yr_full = 2000 + yr if yr < 100 else yr
    return (yr_full, mon, day)

def shift_date_label(shift_str):
    """E.g. '20. May 26' from 'S1 20. May 26'."""
    m = re.search(r'(\d+\.\s+\w+\s+\d+)', shift_str)
    return m.group(1) if m else shift_str

# ── Computed totals ───────────────────────────────────────────────────────────
total_produced   = sum(r[3] for r in RAW if r[3] is not None)
total_good       = sum(r[5] for r in RAW if r[5] is not None)
total_good_first = sum(r[6] for r in RAW if r[6] is not None)
total_ncr        = sum(r[8] for r in RAW if r[8] is not None)
total_rework     = sum(r[10] for r in RAW if r[10] is not None)
total_reintro    = sum(r[15] for r in RAW if r[15] is not None)

fpy = (total_good_first / total_good * 100) if total_good else 0
fpy_class = 'green' if fpy >= 95 else ('alert' if fpy < 90 else 'highlight')

# ── Card 1: avg GPF ratio per hour ───────────────────────────────────────────
hour_gpf = defaultdict(list)
for r in RAW:
    h = extract_hour(r[1])
    if h is not None and r[7] is not None:
        hour_gpf[h].append(r[7])

hour_labels = list(range(24))
hour_avg_gpf = [
    round(sum(hour_gpf[h]) / len(hour_gpf[h]) * 100, 2) if hour_gpf[h] else None
    for h in hour_labels
]

# ── Card 2: by shift ─────────────────────────────────────────────────────────
shift_data = defaultdict(lambda: {'produced': 0, 'good': 0, 'ncr': 0,
                                   'gpf': 0, 'gpf_count': 0, 'rework': 0})
for r in RAW:
    s = r[0]
    if r[3] is not None: shift_data[s]['produced'] += r[3]
    if r[5] is not None: shift_data[s]['good']     += r[5]
    if r[8] is not None: shift_data[s]['ncr']      += r[8]
    if r[6] is not None:
        shift_data[s]['gpf']       += r[6]
    if r[5] is not None and r[6] is not None:
        shift_data[s]['gpf_count'] += r[5]  # denominator = good parts
    if r[10] is not None: shift_data[s]['rework'] += r[10]

sorted_shifts = sorted(shift_data.keys(), key=shift_sort_key)

shift_chart_labels = sorted_shifts
shift_produced_vals = [shift_data[s]['produced'] for s in sorted_shifts]
shift_ncr_vals      = [shift_data[s]['ncr']      for s in sorted_shifts]

# Shorten labels for chart
short_labels = [re.sub(r'^S\d\s+', '', s) for s in sorted_shifts]

# ── Card 3: NCR per hour ──────────────────────────────────────────────────────
hour_ncr = defaultdict(int)
for r in RAW:
    h = extract_hour(r[1])
    if h is not None and r[8] is not None:
        hour_ncr[h] += r[8]

hour_ncr_vals = [hour_ncr[h] for h in hour_labels]

# ── Card 4: daily production ──────────────────────────────────────────────────
day_data = defaultdict(lambda: {'produced': 0, 'good': 0})
for r in RAW:
    if r[0] is None: continue
    dl = shift_date_label(r[0])
    if r[3] is not None: day_data[dl]['produced'] += r[3]
    if r[5] is not None: day_data[dl]['good']     += r[5]

# Sort by date
def date_sort_key(dl):
    m = re.search(r'(\d+)\.\s+(\w+)\s+(\d+)', dl)
    if not m: return (9999,99,99)
    d, mo, yr = int(m.group(1)), MONTH_MAP.get(m.group(2),99), int(m.group(3))
    return (2000+yr if yr<100 else yr, mo, d)

sorted_days = sorted(day_data.keys(), key=date_sort_key)
day_produced_vals = [day_data[d]['produced'] for d in sorted_days]
day_good_vals     = [day_data[d]['good']     for d in sorted_days]

# ── Card 5: reintroduced by shift (top 15) ────────────────────────────────────
reintro_data = defaultdict(lambda: {'reworked': 0, 'total': 0})
for r in RAW:
    s = r[0]
    if s is None: continue
    rw = r[13] if r[13] is not None else 0
    rt = r[15] if r[15] is not None else 0
    reintro_data[s]['reworked'] += rw
    reintro_data[s]['total']    += rt

# sort by total desc, take top 15
top_reintro = sorted(reintro_data.items(), key=lambda x: -x[1]['total'])[:15]
reintro_labels   = [re.sub(r'^S\d\s+', '', s) for s, _ in top_reintro]
reintro_reworked = [d['reworked'] for _, d in top_reintro]
reintro_remain   = [max(0, d['total'] - d['reworked']) for _, d in top_reintro]

# ── Table data (all rows) ─────────────────────────────────────────────────────
def fmt_pct(v):
    if v is None: return '-'
    return f"{v*100:.1f}%"

def badge_gpf(v):
    if v is None: return '<span class="badge info">-</span>'
    if v >= 1.0: return '<span class="badge good">100%</span>'
    if v >= 0.9: return f'<span class="badge warn">{v*100:.1f}%</span>'
    return f'<span class="badge bad">{v*100:.1f}%</span>'

def n(v, decimals=0):
    if v is None: return '-'
    if decimals == 0: return str(int(v))
    return f"{v:.{decimals}f}"

# Build table rows HTML
table_rows_html = []
for r in RAW:
    shift, hour, target, produced, reported, good, gpf, gpf_r, ncr, _, rework, scrap, _, reintro_rw, _, reintro = r
    h_num = extract_hour(hour) if hour else '-'
    table_rows_html.append(f"""
        <tr>
          <td>{shift or '-'}</td>
          <td class="num">{h_num}</td>
          <td class="num">{n(target)}</td>
          <td class="num">{n(produced)}</td>
          <td class="num">{n(reported)}</td>
          <td class="num">{n(good)}</td>
          <td class="num">{n(gpf)}</td>
          <td>{badge_gpf(gpf_r)}</td>
          <td class="num">{n(ncr)}</td>
          <td class="num">{n(rework)}</td>
          <td class="num">{n(scrap)}</td>
          <td class="num">{n(reintro)}</td>
        </tr>""")

table_rows_str = "\n".join(table_rows_html)

# ── Shift table rows ──────────────────────────────────────────────────────────
shift_table_rows = []
for s in sorted_shifts:
    sd = shift_data[s]
    gpf_pct = (sd['gpf'] / sd['gpf_count'] * 100) if sd['gpf_count'] else None
    gpf_str = f"{gpf_pct:.1f}%" if gpf_pct is not None else "-"
    if gpf_pct is not None:
        cls = 'good' if gpf_pct >= 95 else ('warn' if gpf_pct >= 90 else 'bad')
        gpf_badge = f'<span class="badge {cls}">{gpf_str}</span>'
    else:
        gpf_badge = '<span class="badge info">-</span>'
    shift_table_rows.append(f"""
        <tr>
          <td>{s}</td>
          <td class="num">{sd['produced']}</td>
          <td class="num">{sd['good']}</td>
          <td class="num">{sd['ncr']}</td>
          <td>{gpf_badge}</td>
          <td class="num">{sd['rework']}</td>
        </tr>""")

shift_table_str = "\n".join(shift_table_rows)

# ── Insight boxes ─────────────────────────────────────────────────────────────
# Find worst hours for GPF
worst_gpf_hours = [(h, hour_avg_gpf[h]) for h in range(24)
                   if hour_avg_gpf[h] is not None and hour_avg_gpf[h] < 90]
worst_gpf_hours.sort(key=lambda x: x[1])

# Worst shift for NCR
worst_ncr_shift = max(sorted_shifts, key=lambda s: shift_data[s]['ncr'])
worst_ncr_val   = shift_data[worst_ncr_shift]['ncr']

# Day with most reintroduced
top_reintro_shift, top_ri = top_reintro[0] if top_reintro else (None, {'total': 0})

insight1_hours_str = (
    ", ".join([f"Stunde {h} ({v:.0f}%)" for h, v in worst_gpf_hours[:3]])
    if worst_gpf_hours else "keine"
)

today_str = "09.06.2026"
gen_date  = "09.06.2026"

# ── JSON serialisation helpers ────────────────────────────────────────────────
def js_array(lst):
    parts = []
    for v in lst:
        if v is None:
            parts.append('null')
        else:
            parts.append(str(v))
    return '[' + ','.join(parts) + ']'

def js_str_array(lst):
    return json.dumps(lst)

# ── HTML ──────────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Qualitätsauswertung: Good Parts &amp; NCR | DE01 C04-011</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
:root {{
    --atn-green: #B8C400;
    --atn-dark-green: #99CC00;
    --atn-med-green: #CAD340;
    --atn-light-green: #DAE279;
    --atn-pale-green: #EAEDB2;
    --atn-lightest-green: #EDF0BF;
    --black: #000000;
    --dark-grey: #666666;
    --med-grey: #858585;
    --light-grey: #DCDCDC;
    --vlight-grey: #F4F4F4;
    --orange: #E86A10;
    --light-orange: #F1A670;
    --light-blue: #69BBFF;
    --white: #FFFFFF;
    --lightest-green: #EDF0BF;
    --pale-green: #EAEDB2;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family: Arial, Calibri, sans-serif; background:var(--white); color:var(--black); line-height:1.5; font-size:10pt; }}
  .container {{ max-width:1400px; margin:0 auto; padding:24px; }}
  .classification {{ text-align:right; font-style:italic; color:var(--orange); font-size:10pt; padding:8px 0; }}
  header {{ padding:30px 0 20px; border-bottom:2px solid var(--atn-green); margin-bottom:28px; }}
  header h1 {{ font-size:22pt; font-weight:700; color:var(--atn-green); margin-bottom:4px; }}
  header p {{ color:var(--dark-grey); font-size:10pt; }}
  .kpi-row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:14px; margin-bottom:28px; }}
  .kpi {{ background:var(--vlight-grey); border:1px solid var(--light-grey); border-radius:6px; padding:18px; text-align:center; }}
  .kpi .value {{ font-size:26pt; font-weight:700; }}
  .kpi .label {{ font-size:9pt; color:var(--dark-grey); text-transform:uppercase; letter-spacing:.4px; margin-top:4px; }}
  .kpi.alert .value {{ color:var(--orange); }}
  .kpi.green .value {{ color:var(--atn-dark-green); }}
  .kpi.grey .value {{ color:var(--dark-grey); }}
  .kpi.highlight .value {{ color:var(--atn-green); }}
  .card {{ background:var(--white); border:1px solid var(--light-grey); border-radius:6px; padding:22px; margin-bottom:18px; }}
  .card h2 {{ font-size:13pt; font-weight:700; color:var(--atn-green); margin-bottom:14px; }}
  .card h3 {{ font-size:10pt; font-weight:700; color:var(--dark-grey); margin-bottom:10px; text-transform:uppercase; letter-spacing:.4px; }}
  .grid-2 {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; }}
  .grid-3 {{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; }}
  @media(max-width:900px) {{ .grid-2,.grid-3 {{ grid-template-columns:1fr; }} }}
  .chart-wrap {{ position:relative; height:300px; }}
  .chart-wrap.tall {{ height:400px; }}
  table {{ width:100%; border-collapse:collapse; font-size:10pt; }}
  th {{ padding:8px 10px; text-align:left; background:var(--atn-green); color:var(--white); font-weight:700; font-size:9pt; text-transform:uppercase; letter-spacing:.3px; border:1px solid var(--atn-green); }}
  td {{ padding:7px 10px; border:1px solid var(--light-grey); }}
  td.num {{ text-align:right; font-variant-numeric:tabular-nums; }}
  tr:nth-child(even) td {{ background:var(--vlight-grey); }}
  tr:hover td {{ background:var(--lightest-green); }}
  .badge {{ display:inline-block; padding:2px 8px; border-radius:3px; font-size:9pt; font-weight:700; }}
  .badge.good {{ background:var(--pale-green); color:#5a6600; }}
  .badge.warn {{ background:#FEF3C7; color:#92400E; }}
  .badge.bad {{ background:#FEE2E2; color:#991B1B; }}
  .badge.info {{ background:#E0F2FE; color:#075985; }}
  .insight-box {{ background:var(--lightest-green); border:1px solid var(--atn-med-green); border-left:4px solid var(--orange); border-radius:4px; padding:14px 18px; margin-bottom:14px; }}
  .insight-box h4 {{ font-size:10pt; color:var(--black); margin-bottom:3px; }}
  .insight-box p {{ font-size:9pt; color:var(--dark-grey); }}
  .insight-box.info {{ border-left-color:var(--light-blue); }}
  .footer {{ text-align:left; padding:20px 0; color:var(--dark-grey); font-size:8pt; border-top:1px solid var(--light-grey); margin-top:30px; display:flex; justify-content:space-between; }}
  .table-scroll {{ max-height:400px; overflow-y:auto; }}
  @media print {{
    body {{ -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
    .container {{ max-width: 100% !important; padding: 10px; }}
    .card {{ break-inside: avoid; page-break-inside: avoid; }}
    .chart-wrap, .chart-wrap.tall {{ height: 280px; }}
    .kpi-row {{ grid-template-columns: repeat(3, 1fr); }}
    .grid-2, .grid-3 {{ grid-template-columns: 1fr; }}
    table {{ font-size: 8pt; }}
    .badge {{ border: 1px solid #ccc; }}
  }}
</style>
</head>
<body>
<div class="container">

  <div class="classification">- INTERNAL -</div>

  <header>
    <h1>Qualit&auml;tsauswertung: Good Parts &amp; NCR | DE01 C04-011</h1>
    <p>Werk DE01 &nbsp;|&nbsp; Work Center C04-011 &nbsp;|&nbsp; 20.05.2026 &ndash; 09.06.2026</p>
  </header>

  <!-- KPI Row -->
  <div class="kpi-row">
    <div class="kpi grey">
      <div class="value">{total_produced:,}</div>
      <div class="label">Produzierte Teile</div>
    </div>
    <div class="kpi green">
      <div class="value">{total_good:,}</div>
      <div class="label">Good Parts</div>
    </div>
    <div class="kpi {fpy_class}">
      <div class="value">{fpy:.1f}%</div>
      <div class="label">First Pass Yield</div>
    </div>
    <div class="kpi alert">
      <div class="value">{total_ncr:,}</div>
      <div class="label">NCR Teile</div>
    </div>
    <div class="kpi highlight">
      <div class="value">{total_rework:,}</div>
      <div class="label">Rework Teile</div>
    </div>
    <div class="kpi grey">
      <div class="value">{total_reintro:,}</div>
      <div class="label">Reintroduced Parts</div>
    </div>
  </div>

  <!-- Insight Boxes -->
  <div class="insight-box">
    <h4>Kritische Stunden mit niedrigem First-Pass-Yield</h4>
    <p>Folgende Stunden weisen einen durchschnittlichen GPF-Anteil unter 90&nbsp;% auf: {insight1_hours_str}.
       Gezielte Prozessanalysen in diesen Schichtphasen empfohlen.</p>
  </div>
  <div class="insight-box">
    <h4>NCR-Schwerpunkt Schicht {worst_ncr_shift}</h4>
    <p>Die Schicht <strong>{worst_ncr_shift}</strong> verzeichnet mit {worst_ncr_val} NCR-Teilen den h&ouml;chsten Ausschuss im Auswertungszeitraum.
       Eine detaillierte Fehlerursachenanalyse (5-Why / Ishikawa) wird empfohlen.</p>
  </div>
  <div class="insight-box info">
    <h4>Reintroduced Parts &ndash; Handlungsbedarf</h4>
    <p>Insgesamt {total_reintro} Teile wurden als &ldquo;Reintroduced&rdquo; verbucht. Die Schicht <strong>{top_reintro_shift}</strong>
       weist mit {top_ri['total']} Teilen den gr&ouml;&szlig;ten Anteil auf. Davon wurden {top_ri['reworked']} nachgearbeitet.</p>
  </div>

  <!-- Card 1: GPF Ratio per hour -->
  <div class="card">
    <h2>Good Parts First Ratio nach Stunde</h2>
    <div class="chart-wrap">
      <canvas id="chartGpfHour"></canvas>
    </div>
  </div>

  <!-- Card 2: Production by shift -->
  <div class="card">
    <h2>Produktions&uuml;bersicht nach Schicht</h2>
    <div class="grid-2">
      <div>
        <h3>Produzierte Teile &amp; NCR nach Schicht</h3>
        <div class="chart-wrap tall">
          <canvas id="chartShiftBar"></canvas>
        </div>
      </div>
      <div>
        <h3>Schichtdetails</h3>
        <div style="max-height:400px; overflow-y:auto;">
          <table>
            <thead>
              <tr>
                <th>Schicht</th>
                <th>Produziert</th>
                <th>Good Parts</th>
                <th>NCR Teile</th>
                <th>FPY %</th>
                <th>Rework</th>
              </tr>
            </thead>
            <tbody>
{shift_table_str}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Card 3: NCR per hour -->
  <div class="card">
    <h2>NCR-Teile nach Stunde</h2>
    <div class="chart-wrap">
      <canvas id="chartNcrHour"></canvas>
    </div>
  </div>

  <!-- Card 4: Daily production line -->
  <div class="card">
    <h2>Tagesverlauf der Produktion</h2>
    <div class="chart-wrap tall">
      <canvas id="chartDailyLine"></canvas>
    </div>
  </div>

  <!-- Card 5: Reintroduced stacked bar -->
  <div class="card">
    <h2>Reintroduced Parts Analyse (Top 15)</h2>
    <div class="chart-wrap tall">
      <canvas id="chartReintro"></canvas>
    </div>
  </div>

  <!-- Card 6: Full detail table -->
  <div class="card">
    <h2>Detailtabelle: Alle Stunden</h2>
    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>Schicht</th>
            <th>Std</th>
            <th>Ziel</th>
            <th>Produziert</th>
            <th>Reported</th>
            <th>Good Parts</th>
            <th>GPF</th>
            <th>GPF Ratio</th>
            <th>NCR</th>
            <th>Rework</th>
            <th>Scrap</th>
            <th>Reintroduced</th>
          </tr>
        </thead>
        <tbody>
{table_rows_str}
        </tbody>
      </table>
    </div>
  </div>

  <footer class="footer">
    <span>Autoneum Management AG</span>
    <span>Generiert am {gen_date}</span>
  </footer>

</div><!-- /container -->

<script>
// ── Chart 1: GPF Ratio by Hour ───────────────────────────────────────────────
(function(){{
  const labels = {js_str_array([str(h) for h in range(24)])};
  const data   = {js_array(hour_avg_gpf)};
  const ctx = document.getElementById('chartGpfHour').getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels,
      datasets: [{{
        label: 'Ø GPF Ratio (%)',
        data,
        backgroundColor: '#B8C400',
        borderColor: '#99AA00',
        borderWidth: 1,
        borderRadius: 3,
      }}]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }},
        tooltip: {{
          callbacks: {{
            label: ctx => ctx.parsed.y !== null ? ctx.parsed.y.toFixed(1) + ' %' : 'k.A.'
          }}
        }}
      }},
      scales: {{
        y: {{
          min: 0, max: 100,
          title: {{ display: true, text: 'GPF Ratio (%)' }},
          ticks: {{ callback: v => v + ' %' }}
        }},
        x: {{ title: {{ display: true, text: 'Stunde' }} }}
      }}
    }}
  }});
}})();

// ── Chart 2: Shift stacked bar ────────────────────────────────────────────────
(function(){{
  const labels   = {js_str_array(short_labels)};
  const produced = {js_array(shift_produced_vals)};
  const ncr      = {js_array(shift_ncr_vals)};
  const ctx = document.getElementById('chartShiftBar').getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels,
      datasets: [
        {{
          label: 'Produzierte Teile',
          data: produced,
          backgroundColor: '#B8C400',
          borderRadius: 2,
          stack: 'stack',
        }},
        {{
          label: 'NCR Teile',
          data: ncr,
          backgroundColor: '#E86A10',
          borderRadius: 2,
          stack: 'stack',
        }}
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{ legend: {{ position: 'top' }} }},
      scales: {{
        x: {{ stacked: true, ticks: {{ maxRotation: 60, minRotation: 30 }} }},
        y: {{ stacked: true, title: {{ display: true, text: 'Anzahl Teile' }} }}
      }}
    }}
  }});
}})();

// ── Chart 3: NCR by Hour ──────────────────────────────────────────────────────
(function(){{
  const labels = {js_str_array([str(h) for h in range(24)])};
  const data   = {js_array(hour_ncr_vals)};
  const ctx = document.getElementById('chartNcrHour').getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels,
      datasets: [{{
        label: 'NCR Teile',
        data,
        backgroundColor: '#E86A10',
        borderColor: '#C0550A',
        borderWidth: 1,
        borderRadius: 3,
      }}]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{ legend: {{ display: false }} }},
      scales: {{
        y: {{ title: {{ display: true, text: 'NCR Teile (Summe)' }} }},
        x: {{ title: {{ display: true, text: 'Stunde' }} }}
      }}
    }}
  }});
}})();

// ── Chart 4: Daily line chart ─────────────────────────────────────────────────
(function(){{
  const labels   = {js_str_array(sorted_days)};
  const produced = {js_array(day_produced_vals)};
  const good     = {js_array(day_good_vals)};
  const ctx = document.getElementById('chartDailyLine').getContext('2d');
  new Chart(ctx, {{
    type: 'line',
    data: {{
      labels,
      datasets: [
        {{
          label: 'Produzierte Teile',
          data: produced,
          borderColor: '#B8C400',
          backgroundColor: 'rgba(184,196,0,0.12)',
          pointBackgroundColor: '#B8C400',
          tension: 0.3,
          fill: false,
          borderWidth: 2,
          pointRadius: 4,
        }},
        {{
          label: 'Good Parts',
          data: good,
          borderColor: '#666666',
          backgroundColor: 'rgba(102,102,102,0.08)',
          pointBackgroundColor: '#666666',
          tension: 0.3,
          fill: false,
          borderWidth: 2,
          borderDash: [5,3],
          pointRadius: 4,
        }}
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{ legend: {{ position: 'top' }} }},
      scales: {{
        x: {{ ticks: {{ maxRotation: 45, minRotation: 30 }} }},
        y: {{ title: {{ display: true, text: 'Anzahl Teile' }} }}
      }}
    }}
  }});
}})();

// ── Chart 5: Reintroduced stacked bar (top 15) ────────────────────────────────
(function(){{
  const labels   = {js_str_array(reintro_labels)};
  const reworked = {js_array(reintro_reworked)};
  const remain   = {js_array(reintro_remain)};
  const ctx = document.getElementById('chartReintro').getContext('2d');
  new Chart(ctx, {{
    type: 'bar',
    data: {{
      labels,
      datasets: [
        {{
          label: 'Reworked',
          data: reworked,
          backgroundColor: '#69BBFF',
          borderRadius: 2,
          stack: 'ri',
        }},
        {{
          label: 'Übrig (nicht reworked)',
          data: remain,
          backgroundColor: '#E86A10',
          borderRadius: 2,
          stack: 'ri',
        }}
      ]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{ legend: {{ position: 'top' }} }},
      scales: {{
        x: {{ stacked: true, ticks: {{ maxRotation: 60, minRotation: 30 }} }},
        y: {{ stacked: true, title: {{ display: true, text: 'Anzahl Teile' }} }}
      }}
    }}
  }});
}})();
</script>
</body>
</html>
"""

out_path = '/home/user/NVH-2030/report_data5.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Report written to {out_path} ({len(html):,} chars)")
