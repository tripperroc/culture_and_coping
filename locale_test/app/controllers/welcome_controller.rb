class WelcomeController < ApplicationController
  def index
	#flash[:hello] = t(:hello)
	@hello_controller = t(:hello_yml)
  end
end
