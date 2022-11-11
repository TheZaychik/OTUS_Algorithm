package com.company.Task2;

import java.util.ArrayList;

public class ArrayListWrapper<T> {

    private ArrayList<T> array;

    public ArrayListWrapper() {
        array = new ArrayList<>();
    }

    public int size() {
        return array.size();
    }

    public void add(T item) {
        array.add(item);
    }

    public void add(int index, T item) {
        array.add(index, item);
    }

    public T remove(int index) {
        return array.remove(index);
    }

    public T get(int index) {
        return array.get(index);
    }
}