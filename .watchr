watch("less/.*\.less$") do |match|
    system("lessc less/style.less public/css/style.css")
    puts "updating styles."
end
