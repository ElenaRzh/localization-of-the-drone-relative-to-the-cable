| Участник | Роль | Задача |
|----------|------|--------|
| Шерстобитов Олег Андреевич | Программист | Программирование дрона |
| Ржанникова Елена Андреевна | Программист | Работа с ИИ |

## Цель проекта

Создать систему распознования кабеля и позиционирования дрона относительно его.

## Актуальность

Посадка на кабель является самым сложным этапом полета Канатохода. В дальнейшем нашу систему позиционирования относительно кабеля можно будет использовать для автоматизации данного процесса. Это снизит нагрузку на пилотов и требования к их квалификации.

## Описание работы с системой

Дрон в ручном режиме, либо в режиме автономного полета по GPS, сближается с кабелем на расстояние 2-3.5 метра. Две камеры распознают кабель и выводят результаты распознования пилоту, он убеждается в корректности работы системы и подтверждает посадку. Дрон переходит в режим автономного полета и стыкуется с кабелем.
<img src = "https://github.com/user-attachments/assets/88dbae71-9eeb-48e0-ad15-08bfe755d1a2" width="400" height="400">

## Описание системы позиционирования

Две камеры при помощи нейросети вычисляют координаты кабеля в пикселях, каждая от своего лица. Зная угол обзора камеры и ее разерешение, мы находим под каким углом кабель находится относительно камеры и прибавив к этому значению угол наклона самой камеры, мы можем найти под каким углом кабель находится относительно дрона. Так как камеры у нас две, такую операцию мы проделываем дважды. И зная расстояние между камерами, и углы до кабеля, находим координаты кабеля с точностью ≈ 0.01 м.
<img src = "https://github.com/user-attachments/assets/f85cc3e2-4386-4159-8f8e-fdcdf47c9b6e" width = "500" heught = "300">


