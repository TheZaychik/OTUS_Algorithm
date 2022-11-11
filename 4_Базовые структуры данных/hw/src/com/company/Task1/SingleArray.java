package com.company.Task1;

public class SingleArray<T> implements IArray<T> {

    private Object[] array;

    public SingleArray() {
        array = new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void add(T item) {
        resize();
        array[size() - 1] = item;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T) array[index];
    }

    @Override
    public void add(T item, int index) {
        resize();
        int j = 0;
        for (int i = size() - 1; i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = item;

    }

    @Override
    @SuppressWarnings("unchecked")
    public T remove(int index) {
        Object[] newArray = new Object[size() - 1];
        var removed = (T) array[index];
        int j = 0;
        for (int i = 0; i < size(); i++) {
            if (i == index) {
                continue;
            }
            newArray[j] = array[i];
            j++;
        }
        array = newArray;
        return removed;
    }

    private void resize() {
        Object[] newArray = new Object[size() + 1];
        System.arraycopy(array, 0, newArray, 0, size());
        array = newArray;
    }

//    public String toString() {
//        StringBuilder output = new StringBuilder();
//        output.append("[ ");
//        for (int i = 0; i < size(); i++) {
//            output.append(array[i] == null ? "null" : array[i].toString() + " ");
//        }
//        output.append("]");
//        return output.toString();
//    }
}

