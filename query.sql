select 
    *
from booking book, car_detail dtl, car car
where book.car_dtl_id = dtl.car_dtl_id
and dtl.car_id = car.car_id
