#pragma once
#ifndef RECTANGLE_HPP
#define RECTANGLE_HPP

namespace shapes {
    class Rectangle {
        public:
            int x0, y0, x1, y1;
            Rectangle();
            Rectangle(int x0, int y0, int x1, int y1);
            ~Rectangle();
            int getArea();
            void getSize(int* width, int* height);
            void move(int dx, int dy);
    };
}

#endif