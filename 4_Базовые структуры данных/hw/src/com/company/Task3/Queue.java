package com.company.Task3;

import com.company.Task1.SingleArray;

public class Queue<T> {
    private SingleArray<T> array;

    public Queue() {
        array = new SingleArray<>();
    }

    public void enqueue(T item) {
        array.add(item);
    }
    public int size(){
        return array.size();
    }

    public T dequeue() {
        return array.remove(0);
    }
}
