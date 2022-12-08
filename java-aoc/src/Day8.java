import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Day8 {

    public static void main(String[] args) throws Exception {
        Path path = Paths.get("day8/input.txt");
        List<String> lines = Files.readAllLines(path);
        int size = lines.size();
        int[][] terrainMap = new int[size][size];
        int[][] visiblityMap = new int[size][size];
        int[][] scenicMap = new int[size][size];

        int x = 0;
        for(String line : lines) {
            String[] splitted = line.split("");
            for(int y = 0 ; y < size ; y++)
                terrainMap[x][y] = Integer.valueOf( splitted[y]);
            x++;
        }

//        updateVisibility(terrainMap, visiblityMap, size);
        updateScenic(terrainMap, scenicMap, size);

        System.out.println("Terrain map");
        printMap(terrainMap, size);
        System.out.println("Visibility map");
        printMap(visiblityMap, size);
        System.out.println("Scenic map");
        printMap(scenicMap, size);
        int visibleTrees = countVisibleTrees(visiblityMap, size);
        System.out.println("Total number of visible trees: " + visibleTrees);
        int score = countMaxScenicScore(scenicMap, size);
        System.out.println("Highest scenic score: " + score);

    }

    public static int countVisibleTrees(int[][] map, int size) {
        int total = 0;
        for(int y = 0; y < size ; y++)
            for(int x = 0 ; x < size ; x++)
                if(map[y][x] == 1)
                    total+=1;
        return total;
    }

    public static int countMaxScenicScore(int[][] map, int size) {
        int max = 0;
        for(int y = 0; y < size ; y++)
            for(int x = 0 ; x < size ; x++)
                if(map[y][x] > max)
                    max = map[y][x];
        return max;
    }

    public static void updateVisibility(int[][] terrainMap, int[][] visiblityMap, int size) {
        for(int y = 0 ; y < size ; y++)
            for(int x = 0; x < size ; x++) {
                if(isBordered(x, y, size)) {
                    visiblityMap[y][x] = 1;
                    continue;
                }
                if(isVisibleLeft(terrainMap, x, y)) {
                    visiblityMap[y][x] = 1;
                    continue;
                }
                if(isVisibleRight(terrainMap, x, y)) {
                    visiblityMap[y][x] = 1;
                    continue;
                }
                if(isVisibleTop(terrainMap, x, y)) {
                    visiblityMap[y][x] = 1;
                    continue;
                }
                if(isVisibleBottom(terrainMap, x, y)) {
                    visiblityMap[y][x] = 1;
                    continue;
                }
            }
    }

    public static void updateScenic(int[][] terrainMap, int[][] scenicMap, int size) {
        for(int y = 0 ; y < size ; y++)
            for(int x = 0; x < size ; x++)
                scenicMap[y][x] = calculateTreeScenicScore(terrainMap, x, y);
    }

    public static int calculateTreeScenicScore(int[][] terrainMap, int x, int y) {
        int treeHeight = terrainMap[y][x];
        int upPart = calcUpPart(treeHeight, terrainMap, x, y-1);
        int downPart = calcDownPart(treeHeight, terrainMap, x, y+1);
        int leftPart = calcLeftPart(treeHeight, terrainMap, x-1, y);
        int rightPart = calcRightPart(treeHeight, terrainMap, x+1, y);

        System.out.println("Tree " + x + " - " + y + " and height " + terrainMap[y][x] + " has values u:" + upPart + " d:" + downPart + " l:" + leftPart + " r:" + rightPart);
        return upPart * downPart * leftPart * rightPart;
    }

    public static int calcUpPart(int height, int[][] terrainMap, int x, int y) {
        if(y <= 0 || terrainMap[y][x] >= height) {
            return 1;
        } else {
            return 1 + calcUpPart(height, terrainMap, x, y-1);
        }
    }

    public static int calcDownPart(int height, int[][] terrainMap, int x, int y) {
        if(y >= terrainMap[0].length - 1 || terrainMap[y][x] >= height) {
            return 1;
        } else {
            return 1 + calcDownPart(height, terrainMap, x, y+1);
        }
    }


    public static int calcLeftPart(int height, int[][] terrainMap, int x, int y) {
        if(x <= 0 || terrainMap[y][x] >= height) {
            return 1;
        } else {
            return 1 + calcLeftPart(height, terrainMap, x-1, y);
        }
    }

    public static int calcRightPart(int height, int[][] terrainMap, int x, int y) {
        if(x >= terrainMap[0].length - 1 || terrainMap[y][x] >= height) {
            return 1;
        } else {
            return 1 + calcRightPart(height, terrainMap, x+1, y);
        }
    }

    public static boolean isBordered(int x, int y, int size) {
        if(x == 0 || y == 0 || x == size-1 || y == size-1)
            return true;
        return false;
    }

    public static boolean isVisibleLeft(int[][] terrainMap, int x, int y) {
        int treeSize = terrainMap[y][x];
        for(int i = 0 ; i < x; i++) {
            int valueToCheck = terrainMap[y][i];
            if (valueToCheck >= treeSize)
                return false;
        }
        return true;
    }

    public static boolean isVisibleRight(int[][] terrainMap, int x, int y) {
        int treeSize = terrainMap[y][x];
        for(int i = terrainMap.length - 1; i > x; i--)
            if(terrainMap[y][i] >= treeSize)
                return false;
        return true;
    }

    public static boolean isVisibleTop(int[][] terrainMap, int x, int y) {
        int treeSize = terrainMap[y][x];
        for(int i = 0 ; i < y; i++)
            if(terrainMap[i][x] >= treeSize)
                return false;
        return true;
    }

    public static boolean isVisibleBottom(int[][] terrainMap, int x, int y) {
        int treeSize = terrainMap[y][x];
        for(int i = terrainMap.length - 1 ; i > y; i--)
            if(terrainMap[i][x] >= treeSize)
                return false;
        return true;
    }


    public static void printMap(int[][] map, int size) {
        for(int y = 0 ; y < size ; y++) {
            for(int x = 0 ; x < size ; x++)
                System.out.print(map[y][x] + " ");
            System.out.println();
        }


    }

}
