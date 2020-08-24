#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

// The only issue with this question is to find a way to remove duplicates efficiently and to also find the intersection of
// line segments in a efficient manner

// a 2D point
struct Point {
	double x, y;

	// needed for std::unique
	bool operator==(const Point& other) const {
		return x == other.x && y == other.y;
	}
	// needed for std::sort
	bool operator< (const Point& other) const {
		if (x != other.x)
			return x < other.x;
		else
			return y < other.y;
	}
};

// define a segment
struct Segment {
	Point from, to;
};

// find intersection of two segments, out parameter "where" is only valid if function returns true
bool intersect(const Segment& segment1, const Segment& segment2, Point& where) {
	// shorter names for the four endpoints
	auto a = segment1.from;
	auto b = segment1.to;
	auto c = segment2.from;
	auto d = segment2.to;

	// store slope in a Point (just because I'm lazy and don't want to introduce another data type)
	Point slope1, slope2;
	slope1.x = b.x - a.x;
	slope1.y = b.y - a.y;
	slope2.x = d.x - c.x;
	slope2.y = d.y - c.y;

	auto determinant = slope1.x * slope2.y - slope2.x * slope1.y;
	// parallel ?
	if (determinant == 0) {
		return false;
	}

	// now the lines intersect, but not necessarily the segments
	auto s = (slope1.x * (a.y - c.y) - slope1.y * (a.x - c.x)) / determinant;
	auto t = (slope2.x * (a.y - c.y) - slope2.y * (a.x - c.x)) / determinant;

	// parameters s and t must be in (0 ... 1)
	// borders (=endpoints) are not true intersections according to problem statement
	if (s <= 0 || s >= 1 || t <= 0 || t >= 1) {
		return false;
	}

	// yes, intersection found (might be a duplicate, though !)
	where.x = a.x + t * slope1.x;
	where.y = a.y + t * slope1.y;

	// cut off a few digits to avoid rounding issues
	const auto Precision = 0.00000001;
	where.x = round(where.x / Precision) * Precision;
	where.y = round(where.y / Precision) * Precision;

	return true;
}

int main() {
	std::vector<Segment> segments;
	std::vector<Point>   intersections;

	unsigned int limit = 5000;
	unsigned int input[4];
	std::cin >> limit;

	for (unsigned int i = 0; i < limit; i++) {
		// create "random" segment
		Segment current;
		for (unsigned int i = 0; i < 4; i++) {
			std::cin >> input[i];
		}
		current.from.x = input[0];
		current.from.y = input[1];
		current.to.x = input[2];
		current.to.y = input[3];

		// try to intersect with all other segments
		Point where;
		for (auto compare : segments)
			if (intersect(current, compare, where))
				intersections.push_back(where);

		// add current segment to list of segments
		segments.push_back(current);
	}

	// eliminate duplicate intersection points
	std::sort(intersections.begin(), intersections.end());
	auto garbage = std::unique(intersections.begin(), intersections.end());
	intersections.erase(garbage, intersections.end());

	// display result
	std::cout << intersections.size() << std::endl;
	return 0;
}