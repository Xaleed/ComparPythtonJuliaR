function s(n)
    #s = [1/i for i in 1:n]
    s = 0
    for i in 1:n
        s += 1/i
    end
    return(s)
end

s(10)

using BenchmarkTools
J = []
for i in 4:10
    append!(J, @elapsed s(10^i))
end

J
@elapsed s(10^8)
f = []
append!(f, 2)
f
